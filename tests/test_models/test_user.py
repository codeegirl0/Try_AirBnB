#!/usr/bin/python3
"""All unittests user.
All Unittest classes:
    TestUser_inst
    TestUser_saving
    TestUser_to_dicting
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_inst(unittest.TestCase):
    """testing inst."""

    def test_noo_argument_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_nw_inst_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_if_pub_string(self):
        self.assertEqual(str, type(User().id))

    def test_creating_at_is_pub_datime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updating_at_if_pub_datime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_us_unique_ids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_us_different_created_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_us_different_updated_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_arggs_unused(self):
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instan_wth_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_inst_with_noo_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_saving(unittest.TestCase):
    """testing save."""

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
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_savings(self):
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_saving_wth_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_saving_upd_file(self):
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dicting(unittest.TestCase):
    """testing to_dict."""

    def test_to_dicting_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_cor_keys(self):
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_adding_attr(self):
        us = User()
        us.middle_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attr_string(self):
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dicting_output(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_cont_to_dicting_dur_dict(self):
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_wth_argum(self):
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
