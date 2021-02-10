using System.Windows;
using System.Windows.Controls;

namespace RB_Package_Remastered
{
    /// <summary>
    /// Settings.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class Settings : Window
    {
        public Settings()
        {
            InitializeComponent();
            if (AppConfiguration.GetAppConfig("HomePageURL") == "true")
                chk_URL.IsChecked = true;
            if (AppConfiguration.GetAppConfig("URL") == "")
                URL.Text = "https://www.google.co.kr";
            else
                URL.Text = AppConfiguration.GetAppConfig("URL");

            if (AppConfiguration.GetAppConfig("MainUI") == "Default")
                Default.IsChecked = true;
            else
            {
                if (AppConfiguration.GetAppConfig("MainUI") == "Web")
                    Web.IsChecked = true;
                else
                    Offline.IsChecked = true;
            }
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            URL_Change(URL.Text);
        }

        public void URL_Change(string txt)
        {
            AppConfiguration.SetAppConfig("URL", txt);
            // Url 확인용 Console.WriteLine(AppConfiguration.GetAppConfig("URL"));
        }

        private void chk_URL_Checked(object sender, RoutedEventArgs e)
        {
            AppConfiguration.SetAppConfig("HomePageURL", "true");
            URL.IsEnabled = true;
            URL_Reset.IsEnabled = true;
        }

        private void chk_URL_UnChecked(object sender, RoutedEventArgs e)
        {
            AppConfiguration.SetAppConfig("HomePageURL", "false");
            URL.IsEnabled = false;
            URL_Reset.IsEnabled = false;
        }

        private void URL_Reset_Click(object sender, RoutedEventArgs e)
        {
            AppConfiguration.SetAppConfig("HomePageURL", "false");
            URL.Text = "https://www.google.co.kr";
            chk_URL.IsChecked = false;
        }

        private void Default_Checked(object sender, RoutedEventArgs e)
        {
            AppConfiguration.SetAppConfig("MainUI", "Default");
            Web.IsChecked = false;
            Offline.IsChecked = false;
        }

        private void Web_Checked(object sender, RoutedEventArgs e)
        {
            AppConfiguration.SetAppConfig("MainUI", "Web");
            Default.IsChecked = false;
            Offline.IsChecked = false;
        }

        private void Offline_Checked(object sender, RoutedEventArgs e)
        {
            AppConfiguration.SetAppConfig("MainUI", "Offline");
            Default.IsChecked = false;
            Web.IsChecked = false;
        }

        private void Restart_Click(object sender, RoutedEventArgs e)
        {
            Program_Restart();
        }

        private void Program_Restart()
        {
            Application.Current.Shutdown(); // 프로그램 재시작 구문
            System.Windows.Forms.Application.Restart();
        }
        private void Clear_Click(object sender, RoutedEventArgs e)
        {
            if (MessageBox.Show("정말 초기화 하겠습니까?", "초기화 확인", MessageBoxButton.YesNo) == MessageBoxResult.Yes)
            {
                if (MessageBox.Show("비밀번호도 함께 초기화 하시겠습니까?. 암호화된 파일을 다시 복구할 수 없습니다!", "초기화 확인", MessageBoxButton.YesNo) == MessageBoxResult.Yes)
                {
                    AppConfiguration.SetAppConfig("Password", "");
                    Reset();
                }
                else
                    Reset();
            }
        }

        private void Reset()
        {
            AppConfiguration.SetAppConfig("MainUI", "Default");
            AppConfiguration.SetAppConfig("HomePageURL", "false");
            AppConfiguration.SetAppConfig("URL", "https://google.co.kr");
            AppConfiguration.SetAppConfig("Webadress", "false");
            AppConfiguration.SetAppConfig("Link", "");
            Program_Restart();
        }
    }
}