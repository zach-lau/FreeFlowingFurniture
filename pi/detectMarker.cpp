#include <stdio.h>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/aruco.hpp>
#include <iostream>
using namespace cv;	
using namespace std;

//Rotation does not work for n > 1 markers

int main(int argc, char** argv )
{
  VideoCapture inputVideo;
  inputVideo.open(1);

  Mat cameraMatrix, distCoeffs;
  cameraMatrix = (Mat1f(3, 3) << 462.71, 0, 338.630, 0, 465.97, 177.780, 0, 0, 1); //These values should be calibrated
  distCoeffs = (Mat1f(5, 1) << 0.133013, -0.322199, -0.001524, 0.004866, 0.0); //These values should be calibrated

  Ptr<aruco::Dictionary> dictionary = aruco::getPredefinedDictionary(aruco::DICT_6X6_250);

  while(inputVideo.grab())
  {
    Mat image, imageCopy, rot_vec;
    inputVideo.retrieve(image);
    image.copyTo(imageCopy);

    vector<int>ids;
    vector<std::vector<Point2f> > corners;
    aruco::detectMarkers(image, dictionary, corners, ids);

    if(ids.size() > 0)
    {
      aruco::drawDetectedMarkers(imageCopy, corners, ids);

      vector<Vec3d> rvecs, tvecs;
      aruco::estimatePoseSingleMarkers(corners, 0.1, cameraMatrix, distCoeffs, rvecs, tvecs);
      Mat rot_vec;
      
      for(int i=0; i<ids.size(); i++)
      {
        aruco::drawAxis(imageCopy, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.1);
        cout << "coordinates: " << tvecs[i] << endl; //outputs the xyz values of the id marker
        //print the rotation values
        Rodrigues(rvecs[i], rot_vec);
        cout << "rotation xyz: ";
        for(int i=0; i<3; i++)
          cout << rot_vec.at<double>(1,i) << " ";
        cout << endl;
      }
      
    }

    imshow("out", imageCopy);
    char key = (char) waitKey(1);
    if(key == 27)
      break;
  }
  return 0;
}
