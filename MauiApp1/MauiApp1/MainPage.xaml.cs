namespace MauiApp1;

public partial class MainPage : ContentPage
{

	private PlayerViewModel viewModel;
	public MainPage()
	{
		InitializeComponent();
		viewModel = new	PlayerViewModel();
		BindingContext = viewModel;
	}

	private void OnSearchTextChanged(object sender, TextChangedEventArgs e)
	{
		var keyword = e.NewTextValue;
		if (String.IsNullOrWhiteSpace(keyword))
		{
			listView.ItemsSource = viewModel.Players;
		}
		else
		{
			listView.ItemsSource = viewModel.Players
				.Where(plr => plr.Name.ToLower().Contains(keyword.ToLower()));
		}
	}
}

