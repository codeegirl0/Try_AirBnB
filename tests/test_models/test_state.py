#!/usr/bin/python3
"""All unittests state.
The Unittest classes:
    TestState_inst
    TestState_saving
    TestState_to_dicting
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_inst(unittest.TestCase):
    """testing inst."""

    def test_noo_argument_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_nw_inst_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_if_pub_string(self):
        self.assertEqual(str, type(State().id))

    def test_creating_at_is_pub_datime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updating_at_if_pub_datime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_pub_class_attr(self):
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_two_st_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_st_different_created_at(self):
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_two_st_different_updated_at(self):
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        ststr = st.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_arggs_unused(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_instan_wth_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(st.id, "345")
        self.assertEqual(st.created_at, dt)
        self.assertEqual(st.updated_at, dt)

    def test_inst_with_noo_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_saving(unittest.TestCase):
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
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        self.assertLess(first_updated_at, st.updated_at)

    def test_two_savings(self):
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        second_updated_at = st.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        st.save()
        self.assertLess(second_updated_at, st.updated_at)

    def test_saving_wth_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_saving_upd_file(self):
        st = State()
        st.save()
        stid = "State." + st.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


class TestState_to_dicting(unittest.TestCase):
    """testing to_dict."""

    def test_to_dicting_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_cor_keys(self):
        st = State()
        self.assertIn("id", st.to_dict())
        self.assertIn("created_at", st.to_dict())
        self.assertIn("updated_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_to_dict_adding_attr(self):
        st = State()
        st.middle_name = "Holberton"
        st.my_number = 98
        self.assertEqual("Holberton", st.middle_name)
        self.assertIn("my_number", st.to_dict())

    def test_to_dict_datetime_attr_string(self):
        st = State()
        st_dict = st.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dicting_output(self):
        dt = datetime.today()
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(st.to_dict(), tdict)

    def test_cont_to_dicting_dur_dict(self):
        st = State()
        self.assertNotEqual(st.to_dict(), st.__dict__)

    def test_to_dict_wth_argum(self):
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)


if __name__ == "__main__":
    unittest.main()
