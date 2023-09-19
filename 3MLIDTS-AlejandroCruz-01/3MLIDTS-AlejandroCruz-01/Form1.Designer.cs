namespace _3MLIDTS_AlejandroCruz_01
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
            Action3 = new Button();
            Action2 = new Button();
            Action1 = new Button();
            input = new TextBox();
            textBox2 = new TextBox();
            SuspendLayout();
            // 
            // Action3
            // 
            Action3.Location = new Point(349, 193);
            Action3.Name = "Action3";
            Action3.Size = new Size(102, 29);
            Action3.TabIndex = 0;
            Action3.Text = "Clear";
            Action3.UseVisualStyleBackColor = true;
            Action3.Click += Action3_Click;
            // 
            // Action2
            // 
            Action2.Location = new Point(349, 133);
            Action2.Name = "Action2";
            Action2.Size = new Size(102, 29);
            Action2.TabIndex = 1;
            Action2.Text = "<- C to F";
            Action2.UseVisualStyleBackColor = true;
            Action2.Click += Action2_Click;
            // 
            // Action1
            // 
            Action1.Location = new Point(349, 76);
            Action1.Name = "Action1";
            Action1.Size = new Size(102, 27);
            Action1.TabIndex = 2;
            Action1.Text = "F to C ->";
            Action1.UseVisualStyleBackColor = true;
            Action1.Click += Action1_Click;
            // 
            // input
            // 
            input.Location = new Point(113, 76);
            input.Name = "input";
            input.Size = new Size(132, 27);
            input.TabIndex = 3;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(565, 76);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(130, 27);
            textBox2.TabIndex = 4;
            textBox2.TextChanged += textBox2_TextChanged;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(textBox2);
            Controls.Add(input);
            Controls.Add(Action1);
            Controls.Add(Action2);
            Controls.Add(Action3);
            Name = "Form1";
            Text = "Forma 1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button Action3;
        private Button Action2;
        private Button Action1;
        private TextBox input;
        private TextBox textBox2;
    }
}