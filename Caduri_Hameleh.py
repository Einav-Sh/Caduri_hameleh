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

/**
 * This is a demo program showing the use of the DifferentialDrive class, specifically it contains
 * the code necessary to operate a robot with tank drive.
 */
public class Robot extends TimedRobot {
  final private XboxController controller = new XboxController(0);

  final private TalonSRX leftTalon = new TalonSRX(0);
  final private TalonSRX rightTalon = new TalonSRX(1);

  @Override
  public void teleopPeriodic() {
    double leftY = controller.getLeftY();
    double rightX = controller.getRightX();

    leftTalon.set(ControlMode.PercentOutput, leftY); 
    rightTalon.set(ControlMode.PercentOutput, leftY);

    if (rightX > 0) {
      rightTalon.set(ControlMode.PercentOutput, -rightX); 
      leftTalon.set(ControlMode.PercentOutput, rightX);
    }

    if (rightX < 0)
     {rightTalon.set(ControlMode.PercentOutput, rightX); 
      leftTalon.set(ControlMode.PercentOutput, -rightX);
    }
  }
}
