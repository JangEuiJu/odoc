int main()
{
	int n;
	int input;
	int x;

	scanf("%d %d", &n, &x);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &input);
		if (input < x)
			printf("%d ", input);
	}
	


	return 0;
}