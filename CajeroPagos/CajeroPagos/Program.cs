using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CajeroPagos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int option;
            Console.WriteLine("Bienvenido al cajero!");
            int ite = 0;
            do
            {
                Console.WriteLine("1.--Telefono");
                Console.WriteLine("2.--Luz");
                Console.WriteLine("3.--Agua");
                Console.WriteLine("Ingrese el servicio a pagar:");
                option=int.Parse(Console.ReadLine());
                switch(option) 
                {
                    case 1:
                        int montoTotal = 0;
                        String nombre;
                        int[] billetes = new int[10];
                        Console.WriteLine("Ingresó pago de telefono.");
                        Console.WriteLine("Ingrese su nombre:");
                        nombre= Console.ReadLine();
                        while(montoTotal==0 || montoTotal>10000)
                        {
                            Console.WriteLine("Ingrese el monto a pagar:");
                            montoTotal = int.Parse(Console.ReadLine());
                            if(montoTotal > 10000)
                            {
                                Console.WriteLine("Supera el límite de pago");
                            }
                        }
                        Console.WriteLine("El monto total a pagar es de: {0}",montoTotal);
                        int dinero;
                        int total = 0;
                        int indice = 0;
                        while(total < montoTotal)
                        {
                            Console.WriteLine("Ingrese la cantidad digitada:");
                            Console.WriteLine("Billetes aceptados: 50,100,200,500,1000");
                            dinero = int.Parse(Console.ReadLine());
                            if (dinero == 50 || dinero == 100 || dinero == 200 || dinero==500 || dinero == 1000)
                            {
                                Console.WriteLine("Ingresó: {0}", dinero);
                                billetes[indice] = dinero;
                                total += dinero;
                                indice ++;
                                Console.WriteLine("Total= {0}", total);
                            }
                            else
                            {
                                Console.WriteLine("La cantidad no es admitida.");
                                Console.WriteLine("Total={0}", total);
                            }
                        }
                        if(total>montoTotal)
                        {
                            int cambio;
                            cambio = total-montoTotal;
                            Console.WriteLine("Servicio de {0} pagado, el cambio es de: {1}",nombre, cambio);
                        }
                        else
                        {
                            Console.WriteLine("Servicio de {0} pagado.",nombre);
                        }
                        ite += 1;
                        break;
                    case 2:
                        int montoTotal1 = 0;
                        Console.WriteLine("Ingresó pago de luz.");
                        Console.WriteLine("Ingrese su nombre:");
                        nombre= Console.ReadLine();
                        while (montoTotal1 == 0 || montoTotal1 > 10000)
                        {
                            Console.WriteLine("Ingrese el monto a pagar:");
                            montoTotal1 = int.Parse(Console.ReadLine());
                            if (montoTotal1 > 10000)
                            {
                                Console.WriteLine("Supera el límite de pago");
                            }
                        }
                        Console.WriteLine("El monto total a pagar es de: {0}", montoTotal1);
                        total= 0;
                        indice = 0;
                        billetes = new int[10];
                        while(total < montoTotal1)
                        {
                            Console.WriteLine("Ingrese la cantidad digitada:");
                            Console.WriteLine("Billetes aceptados: 50,100,200,1000");
                            dinero = int.Parse(Console.ReadLine());
                            if (dinero == 50 || dinero == 100 || dinero == 200 || dinero == 1000)
                            {
                                Console.WriteLine("Ingresó: {0}", dinero);
                                billetes[indice] = dinero;
                                total += dinero;
                                Console.WriteLine("Total= {0}", total);
                            }
                            else
                            {
                                Console.WriteLine("La cantidad no es admitida.");
                                Console.WriteLine("Total={0}", total);
                            }
                        }
                        if (total > montoTotal1)
                        {
                            int cambio;
                            cambio = total - montoTotal1;
                            Console.WriteLine("Servicio de {0} pagado, el cambio es de: {1}",nombre, cambio);
                        }
                        else
                        {
                            Console.WriteLine("Servicio de {0} pagado.",nombre);
                        }
                        ite += 1;
                        break;
                    case 3:
                        int montoTotal2 = 0;
                        Console.WriteLine("Ingresó pago de agua.");
                        Console.WriteLine("Ingrese su nombre:");
                        nombre= Console.ReadLine();
                        while (montoTotal2 == 0 || montoTotal2 > 10000)
                        {
                            Console.WriteLine("Ingrese el monto a pagar:");
                            montoTotal2 = int.Parse(Console.ReadLine());
                            if (montoTotal2 > 10000)
                            {
                                Console.WriteLine("Supera el límite de pago");
                            }
                        }
                        Console.WriteLine("El monto total a pagar es de: {0}", montoTotal2);
                        total = 0;
                        indice = 0;
                        billetes = new int[10];
                        while (total < montoTotal2)
                        {
                            Console.WriteLine("Ingrese la cantidad digitada:");
                            Console.WriteLine("Billetes aceptados: 50,100,200,1000");
                            dinero = int.Parse(Console.ReadLine());
                            if (dinero == 50 || dinero == 100 || dinero == 200 || dinero == 1000)
                            {
                                Console.WriteLine("Ingresó: {0}", dinero);
                                billetes[indice] = dinero;
                                total += dinero;
                                Console.WriteLine("Total= {0}", total);
                            }
                            else
                            {
                                Console.WriteLine("La cantidad no es admitida.");
                                Console.WriteLine("Total={0}", total);
                            }
                        }
                        if (total > montoTotal2)
                        {
                            int cambio;
                            cambio = total - montoTotal2;
                            Console.WriteLine("Servicio de {0} pagado, el cambio es de: {1}", nombre, cambio);
                        }
                        else
                        {
                            Console.WriteLine("Servicio de {0} pagado.",nombre);
                        }
                        ite += 1;
                        break;
                }
            } while (ite == 0);
        }
    }
}
