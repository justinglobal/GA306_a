class Human(object):
    """A basic class to demonstrate some properties of Python classes"""
    ## constant factor to convert pounds to kilograms
    kPoundsToKg = 0.4536;
    ## constant factor to convert feet to meters
    kFeetToMeters = 0.3048;
    def __init__(self, *args, **kwargs):
        """initialize data attributes from keyword arguments"""
        self.first_name = kwargs.setdefault('first');
        self.last_name = kwargs.setdefault('last');
        self.height = kwargs.setdefault('height');
        self.weight = kwargs.setdefault('weight');
    def bmi(self):
        """compute body mass index assuming metric units"""
        return self.weight / float(self.height)**2;
    @staticmethod
    def get_taller_person(human1, human2):
        """return which of the two instances is taller"""
        if (human1.height > human2.height):
             return human1;
        else: return human2;
    @classmethod
    def create_adam(cls):
        """constructor to create Adam Mechtley"""
        return cls(
            first='Adam',
            last='Mechtley',
            height=6.083*cls.kFeetToMeters,
            weight=172*cls.kPoundsToKg
        );
    # Begin properties
    def fn_getter(self):
        """getter for full name"""
        return '%s %s'%(self.first_name, self.last_name)
    def fn_setter(self, val):
        """setter for full name"""
        self.first_name, self.last_name = val.split()
    ## property for getting and setting the full name
    full_name = property(fn_getter, fn_setter);
    # End properties
    # Alternate property defs for Maya 2010+
    """
    @property
    def full_name(self):
        return '%s %s'%(self.first_name, self.last_name);
    @full_name.setter
    def full_name(self, val):
        self.first_name, self.last_name = val.split();
    """
    def __str__(self):
        """print the full name"""
        return self.full_name;
    def __repr__(self):
        """return a string that can be evaluated"""
        return "Human(%s='%s', %s='%s', %s=%s, %s=%s)"%(
            'first', self.first_name,
            'last', self.last_name,
            'height', self.height,
            'weight', self.weight
        );