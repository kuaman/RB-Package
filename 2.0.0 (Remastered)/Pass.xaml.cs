using System.Windows;
using System.Windows.Input;

namespace RB_Package_Remastered
{
    /// <summary>
    /// Pass.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class Pass : Window
    {
        public Pass()
        {
            InitializeComponent();
        }
        private void CheckBox_Checked(object sender, RoutedEventArgs e)
        {
            noMaskPW.Text = pwBox.Password;
            noMaskPW.Visibility = Visibility.Visible;
            pwBox.Visibility = Visibility.Hidden;
        }

        private void CheckBox_UnChecked(object sender, RoutedEventArgs e)
        {
            pwBox.Password = noMaskPW.Text;
            noMaskPW.Text = null;
            pwBox.Visibility = Visibility.Visible;
            noMaskPW.Visibility = Visibility.Hidden;
        }

        private void KeyEnter(object sender, KeyEventArgs e)
        {
            //decPW
            if (e.Key == Key.Enter) //Enter 누르면
            {
                if (pwBox.Password == Encryption.DecryptString(AppConfiguration.GetAppConfig("Password"), "MaskingPW")) //비밀번호가 일치하면
                {
                    Close(); //Pass창 닫고
                    RB_Editor editor = new RB_Editor(); //RB Editor 실행
                    editor.Show();
                }
            }
        }

        private void KeyEnter1(object sender, KeyEventArgs e)
        {
            //decPW
            if (e.Key == Key.Enter) //Enter 누르면
            {
                if (noMaskPW.Text == Encryption.DecryptString(AppConfiguration.GetAppConfig("Password"), "MaskingPW")) //비밀번호가 일치하면
                {
                    Close(); //Pass창 닫고
                    RB_Editor editor = new RB_Editor(); //RB Editor 실행
                    editor.Show();
                }
            }
        }
    }
}
