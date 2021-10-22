﻿using Microsoft.Win32;
using System.Diagnostics;
using System.Windows;

namespace RB_Package_Remastered
{
    public partial class RB_Link : Window
    {
        public RB_Link()
        {
            InitializeComponent();
        }

        private void TextBox1_Add()
        {
            listBox1.Items.Add(textbox1.Text);
            textbox1.Text = string.Empty;
        }

        private void Add_Click(object sender, RoutedEventArgs e)
        {
            if (textbox1.Text == "")
            {
                OpenFileDialog openFileDialog = new OpenFileDialog();
                if (openFileDialog.ShowDialog() == true)
                {
                    listBox1.Items.Add(openFileDialog.FileName);
                }
            }
            else
                TextBox1_Add();
        }

        private void Del_Click(object sender, RoutedEventArgs e)
        {
            if (listBox1.SelectedIndex == -1)
                return;
            listBox1.Items.RemoveAt(listBox1.SelectedIndex);
        }

        private void TextBox_KeyDown(object sender, System.Windows.Input.KeyEventArgs e)
        {
            if (e.Key == System.Windows.Input.Key.Enter)
            {
                if (textbox1.Text != "")
                    TextBox1_Add();
            }
        }

        private void listBox1_MouseDoubleClick(object sender, System.Windows.Input.MouseButtonEventArgs e)
        {
            try
            {
                Process.Start((string)listBox1.Items.GetItemAt(listBox1.SelectedIndex));
            }
            catch (System.ComponentModel.Win32Exception)
            {
                MessageBox.Show("실행 가능한 프로그램이 없습니다.", "오류");
            }

        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            foreach (var item in Config.Get("Link").ToString().Split(new char[] { ',' }))
            {
                if (!string.IsNullOrEmpty(item))
                    listBox1.Items.Add(item);
            }
        }

        private void Window_Closed(object sender, System.EventArgs e)
        {
            Config.Set("Link", string.Empty);
            foreach (var item in listBox1.Items)
            {
                Config.Add("Link", (string)item);
            }
        }
    }
}
