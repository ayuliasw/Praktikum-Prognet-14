#include <stdio.h>

int luas_persegipanjang() {
	int panjang, lebar, luas;

	scanf("%d", &panjang);
	scanf("%d", &lebar);
	luas = panjang * lebar;
	
	printf(luas);

	return 0;
}

int main() {
	luas_persegipanjang();
}