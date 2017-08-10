# the rotating stage class
#     - wraps around Motor

from Motor import Motor

DEG_PER_CNT = 0.00061035

class Rotator(Motor):

    def __init__(self, ser):
        '''
         Constructor

         ser (Serial): the Serial object that corresponds to the port
         the motor is connected to
        '''

        Motor.__init__(self, ser)
        self.moving = False #set to false
        self.deg_pos = 0    # position of motor, in degrees
        self.deg_zeros = 0    # the origin, in degrees

    def delta_angle(self, deg):    #, m_callback = None, params = ()):
        '''
         Relative rotation on the motor

         deg (float): the degrees of rotation (negative -> counter-clockwise)
        '''
        self.moving = True
        self.deg_pos += deg
        # convert degrees to steps
        steps = int(round(deg / DEG_PER_CNT))

        Motor.delta_move(self, steps)
        self.moving = False

    def abs_angle(self, deg):
        '''
         Relative rotation on the motor

         deg (float): the degrees of rotation (negative -> counter-clockwise)
        '''
        self.moving = True
        # convert degrees to steps
        steps = int(round(deg / DEG_PER_CNT))

        Motor.abs_move(self, steps)
        self.deg_pos = deg
        self.moving = False 

    def get_angle(self):
        '''
         return the motors current position, in degrees
        '''

        return self.deg_pos

    def set_as_zero(self, zer_deg):
        '''
         change the origin (zero)
        '''

        n_zero = int(round(zer_deg / DEG_PER_CNT))
        Motor.set_as_zero(self, n_zero)

        self.deg_zeros = zer_deg
        self.deg_pos -= zer_deg

    def __str__(self):
        '''
         <For Debugging Purposes>
         gives information relevant to the motor state
        '''

        return 'position(degrees): ' + str(self.deg_pos) + '\nzeros-position(degrees): ' + str(self.deg_zeros)
