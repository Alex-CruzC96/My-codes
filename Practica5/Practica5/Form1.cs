using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace Practica5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Mujer_CheckedChanged(object sender, EventArgs e)
        {

        }
        private void Write(String path)
        {
            String name = InputOne.Text.ToString();
            String lastName = Input2.Text.ToString();
            String phone = Input3.Text.ToString();
            float height = float.Parse(Input4.Text);
            String gender = "";
            if (Hombre.Checked)
            {
                gender = Hombre.Text.ToString();
            }
            if (Mujer.Checked)
            {
                gender = Mujer.Text.ToString();
            }
            using (StreamWriter sw = new StreamWriter(path, true))
            {
                sw.WriteLine(name);
                sw.WriteLine(lastName);
                sw.WriteLine(phone);
                sw.WriteLine(height);
                sw.WriteLine(gender);
                sw.WriteLine("\n");
                sw.Close();
            }


        }
        //trabajar con este método
        private void Guardar_Click(object sender, EventArgs e)
        {
            String path = @"C:/Users/alexc/Desktop/Formularios/formulario.txt";
            bool exist = File.Exists(path);
            if (!exist)
            {
                File.Create(path);
            }
            Write(path);
        }

        private void Cancelar_Click(object sender, EventArgs e)
        {
            InputOne.Text = string.Empty;
            Input2.Text = string.Empty;
            Input3.Text = string.Empty;
            Input4.Text = string.Empty;
        }
    }
}