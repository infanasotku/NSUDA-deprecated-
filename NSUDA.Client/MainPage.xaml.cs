namespace NSUDA.Client;
public partial class MainPage : ContentPage
{
	public MainPage()
	{
		InitializeComponent();
	}

	private async Task TestRunXray()
	{
		await CopyFileToAppDataDirectory("config.json", "Xray/Config");
		await CopyFileToAppDataDirectory("xray", "Xray/Executer");
		await CopyFileToAppDataDirectory("geoip.dat", "Xray/Executer");
		await CopyFileToAppDataDirectory("geosite.dat", "Xray/Executer");
		await CopyFileToAppDataDirectory("run.sh", "Xray/Executer");
		string command1 = FileSystem.Current.AppDataDirectory + "/Xray/Executer/xray" + " -c " + FileSystem.Current.AppDataDirectory +
				"/Xray/Config/client_config.json";

        MacShell.Term("chmod u+x " + FileSystem.Current.AppDataDirectory + "/Xray/Executer/xray");
        MacShell.Term(command1);
	}

	

	private async void OnConnectButtonClicked(object sender, EventArgs e)
	{

		if (ConnectButton.Text == "Say yes")
		{
			await Connect();
		}
		else
		{
			Disconnect();
		}
	}
	private async Task Connect()
	{
		bool scenarioResult = true;
		Task run = Task.Run(()=>TestRunXray());

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

	private void Disconnect()
	{
		MacShell.Kill();
		ConnectButton.Text = "Say yes";
		NSUYesLabel.Text = "NSUDA - Say NSU da!";
	}
}

