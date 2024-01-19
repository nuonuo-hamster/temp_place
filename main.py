import cv2
import realsense


def main():
    # Set the size of stream window
    width, height = 640, 480

    # initial camera
    pipe = realsense.realsense_init(width, height)

    while True:

        ######### 相機端 ###########

        # camera run
        depth_frame, color_image, depth_cm = realsense.realsense_run(pipe)
        

        cv2.imshow('RGB Frame', color_image)
        cv2.imshow('Depth Frame', depth_cm)

        if cv2.waitKey(1) == 27: # esc
            break

    cv2.destroyAllWindows()
    pipe.stop()

    ####################################

if __name__ == '__main__':
    main()