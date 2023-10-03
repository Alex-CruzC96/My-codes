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
            InputOne.TextChanged += textChanged;
            
        }

        private void textChanged(object sender, EventArgs e)
        {
            MessageBox.Show("Hola mundo!");
        }
        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Mujer_CheckedChanged(object sender, EventArgs e)
        {

        }
        private String Write(String path)
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
            String datos = $"Nombres: {name}\r\nApellidos: {lastName}\r\nTelefono: {phone}\r\nEstatura: {height}cm\r\nGenero: {gender}";
            return datos;

        }
        //trabajar con este método
        private void Guardar_Click(object sender, EventArgs e)
        {
            String path = @"C:/Users/alexc/Desktop/Formularios/formulario.txt";
            bool exist = File.Exists(path);
            if (!exist)
            {
                File.WriteAllText(path,Write(path));
            }
            else
            {
                using(StreamWriter writer=new StreamWriter(path))
                {
                    if(exist)
                    {
                        writer.WriteLine();
                    }
                    writer.WriteLine(Write(path));
                    MessageBox.Show("Los datos han sido guardados con éxito!");
                }
            }
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