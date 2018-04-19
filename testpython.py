
import maestro
servo = maestro.Controller()
loopv = 'yes'

print('Krafty\'s maestro servo tutorial code demo started \n  (pwm, state (check state), position (check position), speed (set servo speed), range (set servos allowed range of motivation), pause (pause script)')
while loopv == 'yes':
 print('Do:')
 DoVar = raw_input()
 if DoVar == 'pwm':
  print("Channel:")
  cv = input()
  print('Pwm Value:')
  pwmv = input()
  servo.setTarget(int(cv),int(pwmv))  #set servo to move to pwm position

 if DoVar == 'state':
  print('Channel:')
  channelv = input()
  print(servo.isMoving(int(channelv)))

 if DoVar == 'position':
  print('Channel:')
  channelv = input()
  print(servo.getPosition(int(channelv)))

 if DoVar == 'speed':
  print('Channel:')
  channelv = input()
  print('Speed:')
  speedv = input()
  servo.setSpeed(int(channelv), int(speedv))

 if DoVar == 'range':
  print('Channel:')
  channelv = input()
  print('Minimum:')
  minv = input()
  print('Max:')
  maxv = input()
  servo.setRange(int(channelv), int(minv), int(maxv))

 if DoVar == 'pause':
  loopv = 'no'
  servo.stopScript()
 DoVar = ''
 servo.close
