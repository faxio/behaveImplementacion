Feature: GitHub
  
  Scenario: Ver inicio Sesión
     Given Inicio el Navegador Brave
      When Entro a GitHub
      And Click Sign in
      Then Se muestra la página de Inicio de sesión
