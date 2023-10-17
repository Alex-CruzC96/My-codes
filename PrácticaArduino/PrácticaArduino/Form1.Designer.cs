namespace PrácticaArduino
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
            on = new Button();
            off = new Button();
            SuspendLayout();
            // 
            // on
            // 
            on.BackColor = Color.FromArgb(192, 255, 255);
            on.Location = new Point(71, 52);
            on.Name = "on";
            on.Size = new Size(157, 58);
            on.TabIndex = 0;
            on.Text = "Encender";
            on.UseVisualStyleBackColor = false;
            // 
            // off
            // 
            off.BackColor = SystemColors.ActiveBorder;
            off.Location = new Point(71, 182);
            off.Name = "off";
            off.Size = new Size(157, 63);
            off.TabIndex = 1;
            off.Text = "Apagar";
            off.UseVisualStyleBackColor = false;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(301, 343);
            Controls.Add(off);
            Controls.Add(on);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        private Button on;
        private Button off;
    }
}