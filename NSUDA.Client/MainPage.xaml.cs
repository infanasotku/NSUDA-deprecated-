namespace NSUDA.Client;

public partial class MainPage : ContentPage
{

	public MainPage()
	{
		InitializeComponent();
	}

	private async void OnConnectButtonClicked(object sender, EventArgs e)
	{
		if (ConnectButton.Text == "Say yes")
		{
			await Connect();
		}
		else
		{
			await Disconnect();
		}
	}
	private async Task Connect()
	{
		// here we use connection scenario
		bool scenarioResult = true;

		if (scenarioResult)
		{
			ConnectButton.Text = "Disconnect";
			NSUYesLabel.Text = "You said yes!";
			SemanticScreenReader.Announce(ConnectButton.Text);
			SemanticScreenReader.Announce(NSUYesLabel.Text);
		}		
		else
		{
			await DisplayAlert("Error", "Connection not established!",
				"Ok");
		}
	}

	private async Task Disconnect()
	{
			ConnectButton.Text = "Say yes";
			NSUYesLabel.Text = "NSUDA - Say NSU da!";
	}
}

