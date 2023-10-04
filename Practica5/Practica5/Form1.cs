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
        Validar validar=new Validar();
        public Form1()
        {
            InitializeComponent();
            InputOne.TextChanged += validarNombre;
            Input2.TextChanged += validarApellido;
            Input3.TextChanged += validarTelefono;
            Input4.TextChanged += validarEstatura;
        }

        private void validarNombre(object sender, EventArgs e)
        {
            TextBox textBox=(TextBox)sender;
            if (!validar.stringValido(textBox.Text))
            {
                MessageBox.Show("Por favor, ingrese un nombre válido, no utilice carácteres especiales", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //textBox.Clear();
            }
        }
        private void validarEstatura(object sender, EventArgs e)
        {
            TextBox textBox=(TextBox)sender;
            if (!validar.decimalValido(textBox.Text))
            {
                MessageBox.Show("Por favor, ingrese una estatura válida", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //textBox.Clear();
            }
        }
        private void validarApellido(object sender, EventArgs e)
        {
            TextBox textBox=(TextBox)sender;
            if (!validar.stringValido(textBox.Text))
            {
                MessageBox.Show("Por favor, ingrese un apellido válido, no utilice carácteres especiales", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //textBox.Clear();
            }
        }
        private void validarTelefono(object sender, EventArgs e)
        {
            TextBox textBox=(TextBox)sender;
            string input=textBox.Text;
            if(input.Length >= 10)
            {
                if (!validar.longValido(input))
                {
                    MessageBox.Show("Por favor, ingrese un número válido de 10 dígitos", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    //textBox.Clear();
                }
            }
         
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Mujer_CheckedChanged(object sender, EventArgs e)
        {

        }
        
        //trabajar con este método
        private void Guardar_Click(object sender, EventArgs e)
        {
            String name = InputOne.Text;
            String lastName = Input2.Text;
            String phone = Input3.Text;
            String height = Input4.Text;
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
            if (validar.longValido(phone)&&validar.decimalValido(height)&&validar.stringValido(name)&&validar.stringValido(lastName)) {
                String path = @"C:/Users/alexc/Desktop/Formularios/formulario.txt";
                bool exist = File.Exists(path);
                if (!exist)
                {
                    File.WriteAllText(path, datos);
                }
                else
                {
                    using (StreamWriter writer = new StreamWriter(path))
                    {
                        if (exist)
                        {
                            writer.WriteLine();
                        }
                        writer.WriteLine(datos);
                        MessageBox.Show("Los datos han sido guardados con éxito!");
                    }
                }
            }
            else
            {
                MessageBox.Show("Por favor, ingrese datos correctos", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
       
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