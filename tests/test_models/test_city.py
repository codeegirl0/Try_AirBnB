#!/usr/bin/python3
"""All unittests city.
The Unittest classes:
    TestCity_inst
    TestCity_saving
    TestCity_to_dicting
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_inst(unittest.TestCase):
    """testing inst."""

    def test_noo_argument_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_nw_inst_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_if_pub_string(self):
        self.assertEqual(str, type(City().id))

    def test_creating_at_is_pub_datime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updating_at_if_pub_datime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_pub_class_attr(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_ci_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_ci_different_created_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_ci_different_updated_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_arggs_unused(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instan_wth_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_inst_with_noo_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_saving(unittest.TestCase):
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
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_savings(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_saving_wth_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_saving_upd_file(self):
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dicting(unittest.TestCase):
    """testing to_dict."""

    def test_to_dicting_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_cor_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_adding_attr(self):
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attr_string(self):
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dicting_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_cont_to_dicting_dur_dict(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_to_dict_wth_argum(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
