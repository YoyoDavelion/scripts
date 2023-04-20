int main() {
   int opcion;

   while (1) {
      // Mostrar el menú
      setuid(0);
      printf("Elija una opción:\n");
      printf("1. Opción 1\n");
      printf("2. Opción 2\n");
      printf("3. Opción 3\n");
      printf("0. Salir\n");
      printf("> ");

      // Leer la opción elegida
      if (scanf("%d", &opcion) != 1) {
         printf("Entrada inválida\n");
         break;
      }

      // Procesar la opción elegida
      switch (opcion) {
         case 1:
            system("curl -I localhost");
            printf("Ha elegido la opción 1\n");
            break;
         case 2:
            printf("Ha elegido la opción 2\n");
            break;
         case 3:
            printf("Ha elegido la opción 3\n");
            break;
         case 0:
            printf("Saliendo...\n");
            return 0;
         default:
            printf("Opción inválida\n");
            break;
      }
   }
}
