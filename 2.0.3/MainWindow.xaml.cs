using CefSharp.Wpf;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;

namespace RB_Package_Remastered
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            MainUI();
        }

        private void MainUI()
        {
            switch (Config.Get("MainUI"))
            {
                case "Default":
                    InitBrowser(Config.Get("URL"));
                    Search();
                    break;
                case "Web":
                    InitBrowser(Config.Get("URL"));
                    Search();
                    btn_Editor.Visibility = Visibility.Collapsed;
                    btn_Info.Visibility = Visibility.Collapsed;
                    btn_Link.Visibility = Visibility.Collapsed;
                    btn_Settings.Visibility = Visibility.Collapsed;
                    Grid1.ColumnDefinitions.Clear();
                    break;
                case "Offline":
                    ChromeBrowser.Visibility = Visibility.Collapsed;
                    Web.IsEnabled = false;
                    Config.Set("Webadressbar", "false");
                    Grid1.ColumnDefinitions.Clear();
                    break;
            }
        }

        public ChromiumWebBrowser browser;
        private void InitBrowser(string starturl)
        {
            browser = new ChromiumWebBrowser();
            browser.Address = starturl;
            Grid.SetRow(browser, 1);
            Grid1.Children.Add(browser);
        }

        private int search = 0;

        private void Search()
        {
            if (Config.Get("Webadressbar") == "true")
            {
                menu_web.IsChecked = true;
                WebAdress.Visibility = Visibility.Visible;
                WebSearch.Visibility = Visibility.Visible;
                SearchEngine.Visibility = Visibility.Visible;
                switch (Config.Get("SearchEngine"))
                {
                    case "Naver":
                        SearchEngine.Text = "N";
                        search = 1;
                        break;
                    case "Bing":
                        SearchEngine.Text = "B";
                        search = 2;
                        break;
                }
            }
            else
            {
                menu_web.IsChecked = false;
                WebAdress.Visibility = Visibility.Collapsed;
                WebSearch.Visibility = Visibility.Collapsed;
                SearchEngine.Visibility = Visibility.Collapsed;
            }
        }
        private void btn_Editor_Click(object sender, RoutedEventArgs e)
        {
            if (Config.Get("Password") != "")
            {
                Pass PW = new Pass();
                PW.Show();
            }
            else
            {
                Pass_New pass_New = new Pass_New(); //New Pass 실행
                pass_New.Show();
            }
        }

        private void btn_Link_Click(object sender, RoutedEventArgs e)
        {
            RB_Link link = new RB_Link();
            link.Show();
        }

        private void btn_Info_Click(object sender, RoutedEventArgs e)
        {
            Info info = new Info();
            info.ShowDialog();
        }

        private void btn_Settings_Click(object sender, RoutedEventArgs e)
        {
            Settings setting = new Settings();
            setting.ShowDialog();
        }

        private void Update(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("곧 추가됩니다");
        }

        private void web_Checked(object sender, RoutedEventArgs e)
        {
            Config.Set("Webadressbar", "true");
            WebAdress.Visibility = Visibility.Visible;
            WebSearch.Visibility = Visibility.Visible;
            SearchEngine.Visibility = Visibility.Visible;
        }

        private void web_UnChecked(object sender, RoutedEventArgs e)
        {
            Config.Set("Webadressbar", "false");
            WebAdress.Visibility = Visibility.Collapsed;
            WebSearch.Visibility = Visibility.Collapsed;
            SearchEngine.Visibility = Visibility.Collapsed;
        }

        private void webEnter(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Enter)
                browser.Address = WebAdress.Text;
        }

        private void WebSearch_Click(object sender, RoutedEventArgs e)
        {
            switch (search)
            {
                case 0:
                    browser.Address = "https://www.google.com/search?q=" + WebAdress.Text;
                    break;
                case 1:
                    browser.Address = "https://search.naver.com/search.naver?query=" + WebAdress.Text;
                    break;
                case 2:
                    browser.Address = "https://www.bing.com/search?q=" + WebAdress.Text;
                    break;
            }

        }
    }
}
