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
            if (Config.Get("HomePageURL") == "true")
                chk_URL.IsChecked = true;
            if (Config.Get("URL") == "")
                URL.Text = "https://www.google.co.kr";
            else
                URL.Text = Config.Get("URL");
            switch (Config.Get("MainUI"))
            {
                case "Default":
                    Default.IsChecked = true;
                    break;
                case "Web":
                    Web.IsChecked = true;
                    break;
                case "Offline":
                    Offline.IsChecked = true;
                    break;
            }
            switch (Config.Get("SearchEngine"))
            {
                case "Google":
                    SearchEngine_G.IsChecked = true;
                    break;
                case "Naver":
                    SearchEngine_N.IsChecked = true;
                    break;
                case "Bing":
                    SearchEngine_B.IsChecked = true;
                    break;
            }
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            URL_Change(URL.Text);
        }

        public void URL_Change(string txt)
        {
            Config.Set("URL", txt);
            // Url 확인용 Console.WriteLine(Config.Get("URL"));
        }

        private void chk_URL_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("HomePageURL", "true");
            URL.IsEnabled = true;
            URL_Reset.IsEnabled = true;
        }

        private void chk_URL_UnChecked(object sender, RoutedEventArgs e)
        {
            Config.Set("HomePageURL", "false");
            URL.IsEnabled = false;
            URL_Reset.IsEnabled = false;
        }

        private void URL_Reset_Click(object sender, RoutedEventArgs e)
        {
            Config.Set("HomePageURL", "false");
            URL.Text = "https://www.google.co.kr";
            chk_URL.IsChecked = false;
        }

        private void Default_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("MainUI", "Default");
            Web.IsChecked = false;
            Offline.IsChecked = false;
        }

        private void Web_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("MainUI", "Web");
            Default.IsChecked = false;
            Offline.IsChecked = false;
        }

        private void Offline_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("MainUI", "Offline");
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
                switch (MessageBox.Show("비밀번호도 함께 초기화 하시겠습니까?. 암호화된 파일을 다시 복구할 수 없습니다!", "초기화 확인", MessageBoxButton.YesNoCancel))
                {
                    case MessageBoxResult.Yes:
                        Config.Set("Password", "");
                        Reset();
                        break;
                    case MessageBoxResult.No:
                        Reset();
                        break;
                    case MessageBoxResult.Cancel:
                        break;
                }
            }
        }

        private void Reset()
        {
            Config.Set("MainUI", "Default");
            Config.Set("HomePageURL", "false");
            Config.Set("URL", "https://google.co.kr");
            Config.Set("Webadressbar", "false");
            Config.Set("SearchEngine", "Google");
            Config.Set("Link", "");
            Program_Restart();
        }

        private void SearchEngine_G_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("SearchEngine", "Google");
            SearchEngine_N.IsChecked = false;
            SearchEngine_B.IsChecked = false;
        }

        private void SearchEngine_N_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("SearchEngine", "Naver");
            SearchEngine_B.IsChecked = false;
            SearchEngine_G.IsChecked = false;
        }

        private void SearchEngine_B_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("SearchEngine", "Bing");
            SearchEngine_G.IsChecked = false;
            SearchEngine_N.IsChecked = false;
        }
    }
}