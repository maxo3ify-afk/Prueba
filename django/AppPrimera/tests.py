from django.test import TestCase
from .models import Aeropuerto, Vuelo

# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        a1 = Aeropuerto.objects.create(codigo="AAA",ciudad="Ciduad A")
        a2 = Aeropuerto.objects.create(codigo="BBB",ciudad="Ciduad B")

        Vuelo.objects.create(Origen=a1,Destino=a2,Duracion=100)
        Vuelo.objects.create(Origen=a2,Destino=a1,Duracion=100)

    def test_departures_count(self):
        a = Aeropuerto.objects.get(codigo="AAA")
        self.assertEqual(a.arrivals.count(),3)

    def test_arrival_count(self):
        a = Aeropuerto.objects.get(code="AAA")

    def test_valid_flight(self):
        a1 = Aeropuerto.objects.create(codigo="AAA")
        a2 = Aeropuerto.objects.create(codigo="BBB")

        f = Vuelo.objects.get(origen=a1,destino=a2,duracion = 100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1 = Aeropuerto.objects.create(codigo="AAA")
        f = Vuelo.objects.get(Origen=a1,Destino=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1 = Aeropuerto.objects.create(codigo="AAA")
        a2 = Aeropuerto.objects.create(codigo="BBB")
        f = Vuelo.objects.get(Origen=a1, Destino = a2, Duracion=100)