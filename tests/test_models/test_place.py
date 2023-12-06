#!/usr/bin/python3
"""All unittests place.
The Unittest classes:
    TestPlace_inst
    TestPlace_saing
    TestPlace_to_dicting
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_inst(unittest.TestCase):
    """testing inst."""

    def test_noo_argument_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_nw_inst_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_if_pub_string(self):
        self.assertEqual(str, type(Place().id))

    def test_creating_at_is_pub_datime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updating_at_if_pub_datime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_pub_class_attr(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_description_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_two_pl_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_pl_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_pl_different_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_arggs_unused(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instan_wth_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)

    def test_inst_with_noo_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_saing(unittest.TestCase):
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
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_savings(self):
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_saving_wth_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_saving_upd_file(self):
        pl = Place()
        pl.save()
        plid = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dicting(unittest.TestCase):
    """testing to_dict."""

    def test_to_dicting_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_cor_keys(self):
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dict_adding_attr(self):
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_to_dict_datetime_attr_string(self):
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dicting_output(self):
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_cont_to_dicting_dur_dict(self):
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dict_wth_argum(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
