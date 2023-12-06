#!/usr/bin/python3
"""All unittests for amenity.
The Unittest classes:
    TestAmenity_inst
    TestAmenity_saving
    TestAmenity_to_dicting
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_inst(unittest.TestCase):
    """testing instan."""

    def test_noo_argument_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_nw_inst_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_if_pub_string(self):
        self.assertEqual(str, type(Amenity().id))

    def test_creating_at_is_pub_datime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updating_at_if_pub_datime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_pub_class_attr(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amt_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amt_different_created_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amt_different_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_arggs_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instan_wth_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_inst_with_noo_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_saving(unittest.TestCase):
    """testing save method."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_saving(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_savings(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_saving_wth_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_saving_upd_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dicting(unittest.TestCase):
    """testing to_dict."""

    def test_to_dicting_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_cor_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_adding_attr(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attr_string(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dicting_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_cont_to_dicting_dur_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_wth_argum(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
