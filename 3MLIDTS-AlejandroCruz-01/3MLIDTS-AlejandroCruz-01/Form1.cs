namespace _3MLIDTS_AlejandroCruz_01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void Action1_Click(object sender, EventArgs e)
        {
            float f = float.Parse(input.Text);
            float c = (f - 32) * 5.0f / 9.0f;
            textBox2.Text = c.ToString();
        }

        private void Action2_Click(object sender, EventArgs e)
        {
            float c = float.Parse(textBox2.Text);
            float f = (c * 9f / 5f) + 32;
            input.Text = f.ToString();
        }

        private void Action3_Click(object sender, EventArgs e)
        {
            input.Text = null;
            textBox2.Text= null;
        }
    }
}