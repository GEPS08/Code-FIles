package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
// importing

@TeleOp(name = "MovementTest")
public class MovementTest extends LinearOpMode {

  private DcMotor leftMotor;
  private DcMotor rightMotor;
  private DcMotor armMotor;
  
  private Servo leftServo;
  private Servo rightServo;
  // defining the names of the different motors
  
  int prevpos = 0;
  double armpower = 0;
  double armtoggle = 1;
  
  boolean a;
  boolean once = true;
  boolean prevState;

  // defining variables that i use in the rest of the code
  
  void turnLeft(){
    leftMotor = hardwareMap.get(DcMotor.class, "leftMotor");
    rightMotor = hardwareMap.get(DcMotor.class, "rightMotor");
    armMotor = hardwareMap.get(DcMotor.class, "armMotor");
    
    leftServo = hardwareMap.get(Servo.class, "leftServo");
    rightServo = hardwareMap.get(Servo.class, "rightServo");
    //linking the names of the motors to the actual motor hardware
    
    waitForStart();
    rightMotor.setDirection(DcMotorSimple.Direction.REVERSE);
    rightServo.setDirection(Servo.Direction.REVERSE);
    // reversing the diraction of certain motors so that i don't have to do it for every single use of it
    
    leftMotor.setPower(0.5);
    rightMotor.setPower(-0.5);
    sleep(1400);
    leftMotor.setPower(0);
    rightMotor.setPower(0);
  }
  
  void turnRight(){
    leftMotor = hardwareMap.get(DcMotor.class, "leftMotor");
    rightMotor = hardwareMap.get(DcMotor.class, "rightMotor");
    armMotor = hardwareMap.get(DcMotor.class, "armMotor");
    
    leftServo = hardwareMap.get(Servo.class, "leftServo");
    rightServo = hardwareMap.get(Servo.class, "rightServo");
    //linking the names of the motors to the actual motor hardware
    
    waitForStart();
    rightMotor.setDirection(DcMotorSimple.Direction.REVERSE);
    rightServo.setDirection(Servo.Direction.REVERSE);
    // reversing the diraction of certain motors so that i don't have to do it for every single use of it
    
    leftMotor.setPower(-0.5);
    rightMotor.setPower(0.5);
    sleep(1400);
    leftMotor.setPower(0);
    rightMotor.setPower(0);
  }
  
  @Override
  public void runOpMode() {
    leftMotor = hardwareMap.get(DcMotor.class, "leftMotor");
    rightMotor = hardwareMap.get(DcMotor.class, "rightMotor");
    armMotor = hardwareMap.get(DcMotor.class, "armMotor");
    
    leftServo = hardwareMap.get(Servo.class, "leftServo");
    rightServo = hardwareMap.get(Servo.class, "rightServo");
    //linking the names of the motors to the actual motor hardware
    
    waitForStart();
    rightMotor.setDirection(DcMotorSimple.Direction.REVERSE);
    //armMotor.setMode(DcMotor.RunMode RUN_TO_POSITION);
    rightServo.setDirection(Servo.Direction.REVERSE);
    // reversing the diraction of certain motors so that i don't have to do it for every single use of it
    
    while (opModeIsActive()){
      telemetry.addData("left y", gamepad1.right_stick_y);
      telemetry.addData("left x", gamepad1.right_stick_x);
      telemetry.addData("right y", gamepad1.left_stick_y);
      telemetry.addData("right x", gamepad1.left_stick_x);
      telemetry.addData("motors", - gamepad1.right_stick_y + gamepad1.right_stick_x);
      telemetry.addData("dpad up", gamepad1.dpad_up);
      telemetry.addData("dpad down", gamepad1.dpad_down);
      telemetry.addData("dpad left", gamepad1.dpad_left);
      telemetry.addData("dpad right", gamepad1.dpad_right);
      telemetry.addData("arm", gamepad1.left_stick_y * 0.75);
      telemetry.addData("right trigger", gamepad1.right_trigger);
      telemetry.addData("right servo", rightServo.getPosition());
      telemetry.addData("left servo", leftServo.getPosition());
      telemetry.addData("prevpos", prevpos);
      telemetry.addData("currentpos", armMotor.getCurrentPosition());
      telemetry.addData("arm toggle", armtoggle);
      telemetry.addData("bumper", gamepad1.right_bumper);
      telemetry.addData("a", gamepad1.a);
      telemetry.addData("b", gamepad1.b);
      telemetry.addData("y", gamepad1.y);
      telemetry.addData("x", gamepad1.x);
      telemetry.addData("right trigger prevstate", prevState);
      telemetry.addData("once", once);
      // console

      //multiply motorlocktest if movement is too slow
      armMotor.setTargetPosition(armMotor.getCurrentPosition()+gamepad1.left_stick_y);
      
      leftMotor.setPower(- gamepad1.right_stick_y - gamepad1.right_stick_x);
      rightMotor.setPower(- gamepad1.right_stick_y + gamepad1.right_stick_x);
      // setting the rotation of the back two wheels to the x and y values of the right joystick

      armMotor.setPower(gamepad1.left_stick_y * 0.75);
      // setting the position of the arm to the y value of the left joystick
      
      leftServo.scaleRange(0.5, 0.765);
      rightServo.scaleRange(0.355, 0.6);
      // setting bounderies for the servo motors (DO NOT TOUCH)
      
      if (gamepad1.right_trigger != 0){
        armpower = gamepad1.right_trigger;
      }
      
      if (gamepad1.right_bumper){
        if (once){
          if (armtoggle == 0) {
            armtoggle = 1;
          } else if (armtoggle != 0) {
            armtoggle = 0;
          }
          armpower = armtoggle;
          prevState = gamepad1.right_bumper;
        }
        once = false;
      }

      if (!gamepad1.right_bumper && prevState){
        once = true;
        prevState = false;
      }
      // toggling the arm open or closed afer the right bumper button is pressed

      leftServo.setPosition(armpower);
      rightServo.setPosition(armpower);
      // setting the servo's position to the value of the "armpower" variable (1 is closed, 0 is open)

      if (gamepad1.left_stick_y != 0){
        prevpos = armMotor.getCurrentPosition();
      }
      
      if (gamepad1.left_stick_y == 0 && !gamepad1.a){
        if (armMotor.getCurrentPosition() > prevpos){
          armMotor.setPower(-0.2);
          telemetry.addData("arm corrector", "correcting");
        }
      }
      // when the right joystick stopps moving, it records the position of the motor. if the motor has moved from the position recorded, it will move untill it reaches the recorded position
      
      if (gamepad1.dpad_up){
        leftMotor.setPower(0.5);
        rightMotor.setPower(0.5);
      }
      
      if (gamepad1.dpad_down){
        leftMotor.setPower(-0.5);
        rightMotor.setPower(-0.5);
      }
      
      if (gamepad1.dpad_left){
        leftMotor.setPower(0.5);
        rightMotor.setPower(-0.5);
      }
      
      if (gamepad1.dpad_right){
        leftMotor.setPower(-0.5);
        rightMotor.setPower(0.5);
      }
      // checking for each direction of the dpad being pressed
      
      if (gamepad1.a){
        a = true;
        while (a){
          while (armMotor.getCurrentPosition() > -340){
            armMotor.setPower(-0.5);
            prevpos = armMotor.getCurrentPosition();
          }

          while (armMotor.getCurrentPosition() < -340){
            armMotor.setPower(0.3);
            prevpos = armMotor.getCurrentPosition();
          }
          armMotor.setPower(0);
          a = false;
        }
      }
      // once the a button is pressed, the arm will move to the position where it is easiest to pick up cones from the ground
      
      if (gamepad1.b){
        armMotor.setTargetPosition(-340);
        telemetry.addData("helo", 1);
      }
      // make this the arm moving up to put the cone on the pole
      
      if (gamepad1.y){
        turnLeft();
      }
      
      if (gamepad1.x){
        turnRight();
      }

      telemetry.update();
    }
    
    //2.20 sec, 1.55, 2.20, 1.45, 2.20,  -340
  }
}