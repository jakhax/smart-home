from django.test import TestCase
from .models import DeviceTypes,Device

class DeviceTypesTest(TestCase):
    devicetype1 = DeviceTypes(name="lightbulb", iconclass="success", style_type="nb-gear")
    def setUp(self):
        # self.devicetype1 = DeviceTypes(name="lightbulb", iconclass="success", style_type="nb-gear")
        pass
    def tearDown(self):
        # self.device1.delete()
        pass

    @classmethod
    def returndevicetype(cls):
        return cls.devicetype1

    def test_instantiation(self):
        self.assertTrue(isinstance(self.devicetype1, DeviceTypes))

    def test_whether_devicetype_instance_properties_are_correct(self):
        self.assertEquals(self.devicetype1.name,'lightbulb')
        self.assertEquals(self.devicetype1.iconclass,'success')
        self.assertEquals(self.devicetype1.style_type,'nb-gear')

class DeviceTest(TestCase):
    def setUp(self):
        self.device1 = Device(device_type=DeviceTypesTest.returndevicetype() ,room="living", name="lightbulb",pin_number=1, state="False")

    def tearDown(self):
        # self.device1.delete()
        pass
    
    def test_instantiation(self):
        self.assertTrue(isinstance(self.device1, Device))

    def test_whether_device_properties_are_correct(self):
        self.assertEquals(self.device1.name,'lightbulb')
        self.assertEquals(self.device1.name,'lightbulb')
        
        # self.assertEquals(self.device1.iconclass,'success')
        # self.assertEquals(self.device1.style_type,'nb-gear')






