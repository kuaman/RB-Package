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
            if (AppConfiguration.GetAppConfig("MainUI") != "Default")
            {
                if (AppConfiguration.GetAppConfig("MainUI") == "Web")
                {
                    btn_Editor.Visibility = Visibility.Collapsed;
                    btn_Info.Visibility = Visibility.Collapsed;
                    btn_Link.Visibility = Visibility.Collapsed;
                    btn_Settings.Visibility = Visibility.Collapsed;
                    Grid1.ColumnDefinitions.Clear();
                    InitBrowser(AppConfiguration.GetAppConfig("URL"));
                }
                else //Offline
                {
                    ChromeBrowser.Visibility = Visibility.Collapsed;
                    Web.IsEnabled = false;
                    AppConfiguration.SetAppConfig("Webadress", "false");
                    Grid1.ColumnDefinitions.Clear();
                }
            }
            else //Default
            {
                InitBrowser(AppConfiguration.GetAppConfig("URL"));
            }

            if (AppConfiguration.GetAppConfig("Webadress") == "true")
            {
                menu_web.IsChecked = true;
                WebAdress.Visibility = Visibility.Visible;
            }
            else
            {
                menu_web.IsChecked = false;
                WebAdress.Visibility = Visibility.Collapsed;
            }
        }

        public ChromiumWebBrowser browser;
        private void InitBrowser(string starturl)
        {
            // 키보드 자동 팝업 옵션
            //CefSettings settings = new CefSettings();
            //settings.CefCommandLineArgs.Add("disable-usb-keyboard-detect", "1");
            //Cef.Initialize(settings);
            browser = new ChromiumWebBrowser();
            browser.Address = starturl;
            Grid.SetRow(browser, 1);
            Grid1.Children.Add(browser);
        }

        private void btn_Editor_Click(object sender, RoutedEventArgs e)
        {
            if (AppConfiguration.GetAppConfig("Password") != "")
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
            AppConfiguration.SetAppConfig("Webadress", "true");
            WebAdress.Visibility = Visibility.Visible;
        }

        private void web_UnChecked(object sender, RoutedEventArgs e)
        {
            AppConfiguration.SetAppConfig("Webadress", "false");
            WebAdress.Visibility = Visibility.Collapsed;
        }

        private void webEnter(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Enter)
                browser.Address = WebAdress.Text;
        }
    }
}
