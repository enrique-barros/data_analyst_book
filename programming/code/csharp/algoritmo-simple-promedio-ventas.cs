using System;

class Program
{
    static void Main()
    {
        int[] ventas = { 150, 200, 300, 250, 100 };
        int suma = 0;

        foreach (int venta in ventas)
        {
            suma += venta;
        }

        int total = ventas.Length;
        double promedio = (double)suma / total;

        Console.WriteLine("El promedio de ventas es: " + promedio);
    }
}
