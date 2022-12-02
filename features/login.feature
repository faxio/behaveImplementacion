Feature: GitHub
  
  Scenario: Ver inicio Sesión
     Given Inicio el Navegador Brave
      When Entro a GitHub
      And Busco el botón sign in
      Then Se cierra el navegador
