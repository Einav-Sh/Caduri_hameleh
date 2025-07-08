// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot;

import java.nio.channels.Channel;

import javax.xml.stream.events.Comment;

import com.ctre.phoenix.motorcontrol.ControlMode;
import com.ctre.phoenix.motorcontrol.can.TalonSRX;

import edu.wpi.first.util.sendable.SendableRegistry;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.XboxController;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;
import edu.wpi.first.wpilibj.motorcontrol.PWMSparkMax;
import edu.wpi.first.wpilibj.motorcontrol.Talon;
import edu.wpi.first.wpilibj2.command.button.CommandXboxController;

public class Robot extends TimedRobot {
  private final XboxController controller = new XboxController(0);

  private final TalonSRX leftMotorController = new TalonSRX(0);
  private final TalonSRX rightMotorController = new TalonSRX(1);

  @Override
  public void teleopPeriodic() {
    final double leftY = controller.getLeftY();
    final double rightX = controller.getRightX();

    leftMotorController.set(ControlMode.PercentOutput, leftY); 
    rightMotorController.set(ControlMode.PercentOutput, leftY);

    if (rightX > 0) {
      rightMotorController.set(ControlMode.PercentOutput, -rightX); 
      leftMotorController.set(ControlMode.PercentOutput, rightX);
    }

    else if (rightX < 0) {
      rightMotorController.set(ControlMode.PercentOutput, rightX); 
      leftMotorController.set(ControlMode.PercentOutput, -rightX);
    }
  }
}
