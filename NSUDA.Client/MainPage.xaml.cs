namespace NSUDA.Client;

public partial class MainPage : ContentPage
{
	int count = 0;

	public MainPage()
	{
		InitializeComponent();
	}

	private void OnConnectClicked(object sender, EventArgs e)
	{
		count++;

		if (count == 1)
			ConnectBtn.Text = $"Clicked {count} time";
		else
			ConnectBtn.Text = $"Clicked {count} times";

		SemanticScreenReader.Announce(ConnectBtn.Text);
	}
}

