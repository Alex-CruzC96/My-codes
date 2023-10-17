namespace Practica5
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            label1 = new Label();
            Apellido = new Label();
            Telefono = new Label();
            Estatura = new Label();
            Genero = new GroupBox();
            Mujer = new RadioButton();
            Hombre = new RadioButton();
            Guardar = new Button();
            Cancelar = new Button();
            InputOne = new TextBox();
            Input2 = new TextBox();
            Input3 = new TextBox();
            Input4 = new TextBox();
            Genero.SuspendLayout();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(54, 47);
            label1.Name = "label1";
            label1.Size = new Size(67, 20);
            label1.TabIndex = 0;
            label1.Text = "Nombre:";
            label1.Click += label1_Click;
            // 
            // Apellido
            // 
            Apellido.AutoSize = true;
            Apellido.Location = new Point(54, 79);
            Apellido.Name = "Apellido";
            Apellido.Size = new Size(75, 20);
            Apellido.TabIndex = 1;
            Apellido.Text = "Apellidos:";
            // 
            // Telefono
            // 
            Telefono.AutoSize = true;
            Telefono.Location = new Point(54, 111);
            Telefono.Name = "Telefono";
            Telefono.Size = new Size(70, 20);
            Telefono.TabIndex = 2;
            Telefono.Text = "Telefono:";
            // 
            // Estatura
            // 
            Estatura.AutoSize = true;
            Estatura.Location = new Point(54, 143);
            Estatura.Name = "Estatura";
            Estatura.Size = new Size(65, 20);
            Estatura.TabIndex = 3;
            Estatura.Text = "Estatura:";
            // 
            // Genero
            // 
            Genero.Controls.Add(Mujer);
            Genero.Controls.Add(Hombre);
            Genero.Location = new Point(54, 183);
            Genero.Name = "Genero";
            Genero.Size = new Size(291, 58);
            Genero.TabIndex = 5;
            Genero.TabStop = false;
            Genero.Text = "Genero";
            // 
            // Mujer
            // 
            Mujer.AutoSize = true;
            Mujer.Location = new Point(217, 26);
            Mujer.Name = "Mujer";
            Mujer.Size = new Size(68, 24);
            Mujer.TabIndex = 1;
            Mujer.TabStop = true;
            Mujer.Text = "Mujer";
            Mujer.UseVisualStyleBackColor = true;
            Mujer.CheckedChanged += Mujer_CheckedChanged;
            // 
            // Hombre
            // 
            Hombre.AutoSize = true;
            Hombre.Location = new Point(0, 26);
            Hombre.Name = "Hombre";
            Hombre.Size = new Size(85, 24);
            Hombre.TabIndex = 0;
            Hombre.TabStop = true;
            Hombre.Text = "Hombre";
            Hombre.UseVisualStyleBackColor = true;
            // 
            // Guardar
            // 
            Guardar.Location = new Point(72, 261);
            Guardar.Name = "Guardar";
            Guardar.Size = new Size(250, 79);
            Guardar.TabIndex = 6;
            Guardar.Text = "Guardar";
            Guardar.UseVisualStyleBackColor = true;
            Guardar.Click += Guardar_Click;
            // 
            // Cancelar
            // 
            Cancelar.Location = new Point(72, 361);
            Cancelar.Name = "Cancelar";
            Cancelar.Size = new Size(250, 79);
            Cancelar.TabIndex = 7;
            Cancelar.Text = "Cancelar";
            Cancelar.UseVisualStyleBackColor = true;
            Cancelar.Click += Cancelar_Click;
            // 
            // InputOne
            // 
            InputOne.Location = new Point(142, 44);
            InputOne.Name = "InputOne";
            InputOne.Size = new Size(203, 27);
            InputOne.TabIndex = 8;
            InputOne.TextAlign = HorizontalAlignment.Center;
            // 
            // Input2
            // 
            Input2.Location = new Point(142, 79);
            Input2.Name = "Input2";
            Input2.Size = new Size(203, 27);
            Input2.TabIndex = 9;
            Input2.TextAlign = HorizontalAlignment.Center;
            // 
            // Input3
            // 
            Input3.Location = new Point(142, 111);
            Input3.Name = "Input3";
            Input3.Size = new Size(203, 27);
            Input3.TabIndex = 10;
            Input3.TextAlign = HorizontalAlignment.Center;
            // 
            // Input4
            // 
            Input4.Location = new Point(142, 143);
            Input4.Name = "Input4";
            Input4.Size = new Size(203, 27);
            Input4.TabIndex = 11;
            Input4.TextAlign = HorizontalAlignment.Center;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(380, 493);
            Controls.Add(Input4);
            Controls.Add(Input3);
            Controls.Add(Input2);
            Controls.Add(InputOne);
            Controls.Add(Cancelar);
            Controls.Add(Guardar);
            Controls.Add(Genero);
            Controls.Add(Estatura);
            Controls.Add(Telefono);
            Controls.Add(Apellido);
            Controls.Add(label1);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "Form1";
            Text = "Formulario";
            Genero.ResumeLayout(false);
            Genero.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label Apellido;
        private Label Telefono;
        private Label Estatura;
        private GroupBox Genero;
        private RadioButton Mujer;
        private RadioButton Hombre;
        private Button Guardar;
        private Button Cancelar;
        private TextBox InputOne;
        private TextBox Input2;
        private TextBox Input3;
        private TextBox Input4;
    }
}