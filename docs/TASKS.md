# Backlog zadań

> **Uwaga:** Nie znaleziono pliku `docs/PRD.md` w repozytorium. Lista zadań została przygotowana na podstawie standardowych wymagań dla konfiguratorów Langfuse oraz nazwy projektu. W razie dostarczenia PRD dokument należy zrewidować.

## 1. Discovery i dokumentacja
- [ ] Zweryfikować zakres projektu z Product Ownerem i potwierdzić wymagania opisane w docelowym `PRD.md`.
- [ ] Przygotować diagram architektury integracji Langfuse (komponenty backendu, SDK, przepływ danych telemetrycznych).
- [ ] Ustalić politykę przechowywania sekretów (API key Langfuse, klucze usług pomocniczych) i spisać ją w `docs/SECURITY.md`.

## 2. Backend
- [ ] Utworzyć usługę konfiguracji Langfuse zapewniającą endpointy REST/GraphQL do zapisu ustawień organizacji (URL serwisu, klucze API, środowiska).
- [ ] Dodać warstwę walidacji danych wejściowych (np. schematy Zod/JOI) oraz obsługę błędów zewnętrznego API Langfuse.
- [ ] Zaimplementować scheduler synchronizacji konfiguracji, który cyklicznie weryfikuje status połączenia z Langfuse i raportuje alerty.

## 3. Frontend / Panel administracyjny
- [ ] Stworzyć UI kreatora konfiguracji (etapy: wprowadzenie danych, test połączenia, wybór integracji językowych/SDK).
- [ ] Zapewnić komponent podglądu logów/testowych wywołań Langfuse oraz sekcję diagnostyki błędów.
- [ ] Dodać ekran zarządzania środowiskami (dev/stage/prod) z możliwością generowania tokenów i przypisywania ról użytkownikom.

## 4. Integracje i SDK
- [ ] Przygotować paczkę SDK (Node.js/Python) z gotową konfiguracją Langfuse oraz przykładami instrumentacji.
- [ ] Stworzyć przykładową aplikację demo pokazującą integrację Langfuse z popularnym frameworkiem (np. Next.js).
- [ ] Opracować skrypty automatyzujące dodawanie middleware/loggingu Langfuse do istniejących projektów.

## 5. DevOps i infrastruktura
- [ ] Skonfigurować CI/CD (lint, testy, build) oraz automatyczne publikowanie paczek SDK.
- [ ] Przygotować IaC (Terraform/Pulumi) dla wymaganych zasobów chmurowych (sekrety, kolejki, monitoring).
- [ ] Zaimplementować monitoring i alerting dla usług integracyjnych (np. Prometheus + Grafana lub Langfuse dashboards).

## 6. QA i bezpieczeństwo
- [ ] Przygotować plan testów end-to-end obejmujący scenariusze sukcesu i błędów komunikacji z Langfuse.
- [ ] Dodać testy bezpieczeństwa (skanowanie sekretów, SAST, dependency scanning) do pipeline'u.
- [ ] Przeprowadzić audyt zgodności z RODO (PII w logach) i wdrożyć mechanizmy anonimizacji danych.

## 7. Wdrożenie i edukacja
- [ ] Przygotować dokumentację wdrożeniową i FAQ dla zespołów developerskich korzystających z konfiguratora.
- [ ] Stworzyć warsztat/onboarding (prezentacja + nagranie) pokazujący proces konfiguracji Langfuse krok po kroku.
- [ ] Zebrać feedback od pierwszych użytkowników i przygotować backlog usprawnień (np. w systemie ticketowym).
