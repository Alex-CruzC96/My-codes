using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Practica5
{
    internal class Validar
    {
        public bool stringValido(string value)
        {
            return Regex.IsMatch(value, @"[a-zA-Z\s]+$");
        }
        public bool decimalValido(string value)
        {
            decimal result;
            return decimal.TryParse(value, out result);
        }
        public bool longValido(String value)
        {
            long result;
            return long.TryParse(value, out result) && value.Length == 10;
        }
    }
}
