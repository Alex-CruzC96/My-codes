namespace FormulaGeneral
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
            label1 = new Label();
            textA = new Label();
            textB = new Label();
            textC = new Label();
            inputA = new TextBox();
            inputB = new TextBox();
            inputC = new TextBox();
            label2 = new Label();
            label3 = new Label();
            output1 = new TextBox();
            output2 = new TextBox();
            evento = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Arial", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(6, 9);
            label1.Name = "label1";
            label1.Size = new Size(305, 24);
            label1.TabIndex = 0;
            label1.Text = "Calculadora de formula general";
            // 
            // textA
            // 
            textA.AutoSize = true;
            textA.Location = new Point(12, 79);
            textA.Name = "textA";
            textA.Size = new Size(98, 20);
            textA.TabIndex = 1;
            textA.Text = "Coeficiente A";
            // 
            // textB
            // 
            textB.AutoSize = true;
            textB.Location = new Point(12, 133);
            textB.Name = "textB";
            textB.Size = new Size(97, 20);
            textB.TabIndex = 2;
            textB.Text = "Coeficiente B";
            // 
            // textC
            // 
            textC.AutoSize = true;
            textC.Location = new Point(12, 190);
            textC.Name = "textC";
            textC.Size = new Size(97, 20);
            textC.TabIndex = 3;
            textC.Text = "Coeficiente C";
            textC.UseMnemonic = false;
            // 
            // inputA
            // 
            inputA.Location = new Point(168, 72);
            inputA.Name = "inputA";
            inputA.Size = new Size(129, 27);
            inputA.TabIndex = 4;
            inputA.TextAlign = HorizontalAlignment.Center;
            // 
            // inputB
            // 
            inputB.Location = new Point(168, 130);
            inputB.Name = "inputB";
            inputB.Size = new Size(129, 27);
            inputB.TabIndex = 5;
            inputB.TextAlign = HorizontalAlignment.Center;
            // 
            // inputC
            // 
            inputC.Location = new Point(168, 187);
            inputC.Name = "inputC";
            inputC.Size = new Size(129, 27);
            inputC.TabIndex = 6;
            inputC.TextAlign = HorizontalAlignment.Center;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(12, 272);
            label2.Name = "label2";
            label2.Size = new Size(24, 20);
            label2.TabIndex = 7;
            label2.Text = "x1";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(168, 272);
            label3.Name = "label3";
            label3.Size = new Size(24, 20);
            label3.TabIndex = 8;
            label3.Text = "x2";
            // 
            // output1
            // 
            output1.Location = new Point(37, 269);
            output1.Name = "output1";
            output1.Size = new Size(72, 27);
            output1.TabIndex = 9;
            output1.TextAlign = HorizontalAlignment.Center;
            // 
            // output2
            // 
            output2.Location = new Point(198, 269);
            output2.Name = "output2";
            output2.Size = new Size(82, 27);
            output2.TabIndex = 10;
            output2.TextAlign = HorizontalAlignment.Center;
            // 
            // evento
            // 
            evento.Location = new Point(96, 339);
            evento.Name = "evento";
            evento.Size = new Size(126, 41);
            evento.TabIndex = 11;
            evento.Text = "Calcular";
            evento.UseVisualStyleBackColor = true;
            evento.Click += evento_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(323, 450);
            Controls.Add(evento);
            Controls.Add(output2);
            Controls.Add(output1);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(inputC);
            Controls.Add(inputB);
            Controls.Add(inputA);
            Controls.Add(textC);
            Controls.Add(textB);
            Controls.Add(textA);
            Controls.Add(label1);
            Name = "Form1";
            Text = "Formula General";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label textA;
        private Label textB;
        private Label textC;
        private TextBox inputA;
        private TextBox inputB;
        private TextBox inputC;
        private Label label2;
        private Label label3;
        private TextBox output1;
        private TextBox output2;
        private Button evento;
    }
}