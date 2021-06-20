using Microsoft.Win32;
using System.IO;
using System.Windows;

namespace RB_Package_Remastered
{
    public partial class RB_Editor : Window
    {
        private string decPW = Encryption.DecryptString(Config.Get("Password"), "*****");
        private int a = 0;
        public RB_Editor()
        {
            InitializeComponent();
        }

        private void Load_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Text file (*.txt)|*.txt|RB Secure file(*.rbs)|*.rbs";
            if (openFileDialog.ShowDialog() == true)
            {
                if (Path.GetExtension(openFileDialog.FileName) == ".rbs")
                {
                    TextBox1.Text = Encryption.DecryptString(File.ReadAllText(openFileDialog.FileName), decPW);
                }
                else
                {
                    TextBox1.Text = File.ReadAllText(openFileDialog.FileName);
                }
                this.Title += " + " + openFileDialog.FileName;
            }
        }

        private void Save_Click(object sender, RoutedEventArgs e)
        {
            if (a == 2) //No enc (.txt)
            {
                SaveFileDialog saveFileDialog = new SaveFileDialog();
                saveFileDialog.Filter = "Text file (*.txt)|*.txt";    //"Text file (*.txt)|*.txt|C# file (*.cs)|*.cs";
                if (saveFileDialog.ShowDialog() == true)
                {
                    File.WriteAllText(saveFileDialog.FileName, TextBox1.Text);
                }
                this.Title += " + " + saveFileDialog.FileName;
            }
            else //enc (.rbs)
            {
                SaveFileDialog saveFileDialog = new SaveFileDialog();
                saveFileDialog.Filter = "RB Secure file(*.rbs)|*.rbs";    //"Text file (*.txt)|*.txt|C# file (*.cs)|*.cs";
                if (saveFileDialog.ShowDialog() == true)
                {
                    File.WriteAllText(saveFileDialog.FileName, Encryption.EncryptString(TextBox1.Text, decPW));
                }
                this.Title += " + " + saveFileDialog.FileName;
            }
        }

        private void save_enc_Checked(object sender, RoutedEventArgs e)
        {
            a = 1;
        }

        private void save_enc_UnChecked(object sender, RoutedEventArgs e)
        {
            a = 2;
        }

        private void pre_enc_Checked(object sender, RoutedEventArgs e)
        {
            TextBox1.Text = Encryption.EncryptString(TextBox1.Text, decPW);
        }

        private void pre_enc_Unchecked(object sender, RoutedEventArgs e)
        {
            TextBox1.Text = Encryption.DecryptString(TextBox1.Text, decPW);
        }
    }
}