# 🇫🇷 Documentation en Français - CodigoFest 2023

## Découvrez les Nouveautés de l'IA dans l'Écosystème Azure

Cette documentation fournit un guide complet des démos et du contenu présentés à CodigoFest 2023.

---

## 📑 Table des Matières

1. [Introduction](#introduction)
2. [Serveurs MCP](#serveurs-mcp)
3. [Agents avec Microsoft Agent Framework](#agents-avec-microsoft-agent-framework)
4. [Projets C# Agent Framework](#projets-c-agent-framework)
5. [Guides d'Installation et d'Utilisation](#guides-dinstallation-et-dutilisation)
6. [Exemples d'Utilisation](#exemples-dutilisation)
7. [Dépannage](#dépannage)

---

## 🎯 Introduction

Ce dépôt démontre les capacités les plus avancées de l'Intelligence Artificielle dans l'écosystème Azure, en se concentrant sur :

- **Model Context Protocol (MCP)** : Protocole standard pour connecter des outils et des données avec des systèmes d'IA
- **Microsoft Agent Framework** : Framework pour construire des agents intelligents capables de raisonner et d'exécuter des tâches
- **Azure AI Foundry** : Plateforme complète pour développer, entraîner et déployer des solutions d'IA
- **Intégration Hugging Face** : Génération d'images avec des modèles avancés

### Qu'est-ce que le Model Context Protocol (MCP) ?

MCP est un protocole ouvert qui standardise la façon dont les applications fournissent du contexte aux grands modèles de langage (LLMs). Il permet aux agents IA d'accéder à :
- Données d'entreprise
- Outils et APIs
- Services externes
- Systèmes de fichiers locaux

---

## 🏆 Serveurs MCP

### 1. Serveur World Cup 2026 Info

Serveur MCP spécialisé qui fournit des informations complètes sur la Coupe du Monde FIFA 2026.

#### 📋 Fonctionnalités

- **Informations sur le Tournoi** : Dates, sites, nombre d'équipes et de matchs
- **Villes Hôtes** : Détails des 16 villes hôtes et de leurs stades
- **Calendrier des Matchs** : Structure du tournoi et dates clés
- **Données Historiques** : Faits uniques sur cette coupe du monde historique

#### 🔧 Outils Disponibles

1. **get_tournament_info()**
   - Retourne les informations générales du tournoi
   - Aucun paramètre requis
   - Réponse au format JSON

2. **get_host_cities(country: Optional[str])**
   - Obtient des informations sur les villes hôtes
   - Paramètre optionnel : filtrer par pays ('United States', 'Canada', 'Mexico')
   - Inclut le nom du stade, la capacité et les types de matchs

3. **get_match_schedule()**
   - Retourne la structure du tournoi et le calendrier
   - Informations sur la phase de groupes et les éliminatoires
   - Dates clés et notes spéciales

#### 📊 Données de la Coupe du Monde 2026

```json
{
  "nom": "Coupe du Monde FIFA 2026",
  "hôtes": ["États-Unis", "Canada", "Mexique"],
  "dates": "11 juin - 19 juillet 2026",
  "équipes": 48,
  "matchs": 104,
  "stades": 16,
  "première_coupe_trois_nations": true
}
```

#### 🎯 Cas d'Usage

```python
# Exemple 1 : Informations générales du tournoi
await get_tournament_info()

# Exemple 2 : Villes des États-Unis
await get_host_cities(country="United States")

# Exemple 3 : Calendrier complet
await get_match_schedule()
```

#### 🚀 Comment Exécuter

```bash
cd MCP/worldcup-info

# Option 1 : Utiliser uv (recommandé)
uv venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
uv pip install -r pyproject.toml --extra dev

# Option 2 : Utiliser pip
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Déboguer avec Agent Builder (VS Code)
# Appuyez sur F5 et sélectionnez "Debug in Agent Builder"
```

#### 🧪 Tester avec MCP Inspector

```bash
cd inspector
npm install

# Démarrer Inspector (depuis le panneau Debug de VS Code)
# Sélectionnez "Debug SSE in Inspector (Edge)" ou "(Chrome)"
# F5 pour démarrer

# Dans le navigateur :
# 1. Cliquez sur "Connect"
# 2. Sélectionnez "List Tools"
# 3. Choisissez un outil et exécutez-le
```

### 2. Serveur Sample Weather

Serveur MCP d'exemple qui fournit des données météorologiques simulées.

#### 📋 Fonctionnalités

- Serveur simple pour démonstration
- Données météorologiques aléatoires
- Base pour créer des serveurs MCP personnalisés

#### 🔧 Outils Disponibles

1. **get_weather(location: str)**
   - Retourne des informations météorologiques simulées
   - Paramètre requis : localisation (ville, état, coordonnées)
   - Réponse avec température et condition météorologique

#### 🎯 Exemple d'Utilisation

```python
# Interroger la météo d'une ville
await get_weather(location="Toronto")

# Exemple de réponse :
# {
#   "location": "Toronto",
#   "temperature": "72°F",
#   "condition": "Sunny"
# }
```

#### 🚀 Comment Exécuter

```bash
cd MCP/SampleWeather

# Configurer l'environnement
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Déboguer avec Agent Builder
# F5 dans VS Code avec "Debug in Agent Builder"
```

---

## 🤖 Agents avec Microsoft Agent Framework

### WorldCup Info Agent v1

Agent intelligent qui combine des requêtes sur la Coupe du Monde 2026 avec la génération d'images en style pixel art.

#### 🎨 Capacités Principales

1. **Requêtes Informatives**
   - Répond aux questions sur la Coupe du Monde 2026
   - Accède aux données en temps réel via MCP
   - Fournit des informations précises et actualisées

2. **Génération d'Images**
   - Génère des images en style pixelisé (pixel art, 8-bit)
   - Utilise le modèle FLUX1 Schnell via Hugging Face
   - Paramètres personnalisables (taille, seed, étapes)

3. **Conversation Multi-tours**
   - Maintient le contexte entre les questions
   - Thread persistant pour des conversations cohérentes
   - Traitement des réponses en streaming

#### ⚙️ Configuration Technique

```python
# Point de terminaison Azure AI Foundry
ENDPOINT = "https://bruno-realtime-resource.services.ai.azure.com/api/projects/bruno-realtime"
MODEL_DEPLOYMENT_NAME = "gpt-5-mini"

# Outils MCP
MCPStreamableHTTPTool(
    name="brunoHF",
    description="Serveur MCP pour brunoHF",
    url="https://huggingface.co/mcp?login"
)
```

#### 📝 Instructions de l'Agent

L'agent est configuré pour :

- **Langue** : Espagnol (par défaut), adaptable selon la demande de l'utilisateur
- **Génération d'Images** : Toujours en style pixelisé utilisant FLUX1 Schnell
- **Format de Réponse** : JSON structuré avec raisonnement et conclusion
- **Sécurité** : Évite le contenu protégé par le droit d'auteur, offre des alternatives légales

#### 🔄 Flux de Travail

```
Utilisateur → Question
    ↓
Agent → Analyse l'intention
    ↓
Nécessite image ? → OUI → Génère un prompt descriptif
    |                         ↓
    |                    Appelle gr1_flux1_schnell_infer
    |                         ↓
    NON                  Reçoit l'URL de l'image
    ↓                         ↓
Interroge le serveur MCP ← ← ← ←
    ↓
Construit une réponse structurée
    ↓
Utilisateur ← Réponse JSON
```

#### 💬 Exemples de Conversation

**Exemple 1 : Requête Informative**
```
Utilisateur : "Quel temps fait-il à Toronto ?"

Agent :
{
  "location": "Toronto",
  "temperature": "72°F",
  "condition": "Sunny"
}
```

**Exemple 2 : Génération d'Image**
```
Utilisateur : "Pouvez-vous générer une image d'un raton laveur jouant au football à la Coupe du Monde 2026 ?"

Agent :
{
  "input": "Générer image de raton laveur jouant au football à la Coupe du Monde 2026",
  "reasoning": [
    "L'utilisateur demande une image, elle doit être générée en style pixelisé",
    "Utiliser l'outil gr1_flux1_schnell_infer de Hugging Face",
    "Éviter les logos officiels en raison du droit d'auteur"
  ],
  "response": "J'ai généré une image pixelisée en style 8-bit d'un raton laveur jouant au football. L'image a un style rétro de jeu vidéo classique.",
  "image": {
    "requested": true,
    "model_used": "evalstate/flux1_schnell",
    "generation_parameters": {
      "prompt": "Pixel art 8-bit raccoon playing soccer at World Cup 2026, wearing jersey, kicking ball in stadium, crowd in background, retro video game style, limited color palette, blocky sprites, nostalgic gaming aesthetic",
      "width": 1024,
      "height": 1024,
      "num_inference_steps": 4,
      "randomize_seed": true
    },
    "image_url": "https://huggingface.co/.../image.png",
    "notes": "Image sans logos officiels pour éviter les problèmes de droit d'auteur"
  }
}
```

#### 🚀 Comment Exécuter

```bash
# Installer les dépendances
pip install agent-framework
pip install agent-framework-azure-ai
pip install azure-identity

# Configurer les variables d'environnement (ou éditer le script)
export AZURE_AI_ENDPOINT="votre-endpoint"
export AZURE_AI_MODEL="votre-modèle"

# Exécuter l'agent
cd Agents
python worldcupinfo-v1.py
```

#### 🔑 Prérequis

- Projet Azure AI Foundry
- Azure Default Credential configuré
- Token Hugging Face (pour la génération d'images)
- Python 3.8+

#### 🎛️ Paramètres de Génération d'Images

```python
generation_parameters = {
    "prompt": "Description détaillée (60-70 mots)",
    "width": 1024,           # Plage : 256-2048
    "height": 1024,          # Plage : 256-2048
    "seed": 123456789,       # Optionnel : 0-2147483647
    "randomize_seed": True,  # Si True, seed aléatoire
    "num_inference_steps": 4 # Plage : 1-16
}
```

---

## 🔧 Projets C# Agent Framework

### Structure des Projets

Le répertoire `src/` contient trois projets d'exemple en C# démontrant l'utilisation d'Agent Framework :

```
src/
├── AgentFx-01/
│   ├── Program.cs
│   └── AgentFx-01.csproj
├── AgentFx-02/
│   ├── Program.cs
│   └── AgentFx-02.csproj
└── AgentFx-03/
    ├── Program.cs
    └── AgentFx-03.csproj
```

### État Actuel

Actuellement, ces projets contiennent des modèles "Hello World" de base. Ce sont des points de départ pour :

1. **Intégration avec Azure AI Services**
2. **Implémentation d'agents en .NET**
3. **Connexion aux serveurs MCP depuis C#**
4. **Construction d'applications d'entreprise avec des agents**

### 🚀 Compiler et Exécuter

```bash
cd src/AgentFx-01

# Restaurer les dépendances
dotnet restore

# Compiler
dotnet build

# Exécuter
dotnet run
```

### 🔜 Développement Futur

Ces projets sont prêts à implémenter :

- ✅ Agents conversationnels en C#
- ✅ Intégration avec Azure OpenAI
- ✅ Connexion avec serveurs MCP
- ✅ Traitement de documents
- ✅ Automatisation d'entreprise

---

## 📚 Guides d'Installation et d'Utilisation

### Exigences Système

#### Logiciels Requis
- **Python** : 3.8 ou supérieur
- **Node.js** : 16.x ou supérieur (pour MCP Inspector)
- **.NET SDK** : 6.0 ou supérieur (pour projets C#)
- **Visual Studio Code** : Dernière version
- **Git** : Pour cloner le dépôt

#### Extensions VS Code Recommandées
- AI Toolkit for VS Code
- Python Extension
- C# Extension
- Python Debugger

### Configuration Azure

#### 1. Projet Azure AI Foundry

```bash
# Créer un projet dans Azure AI Foundry
# 1. Aller sur https://ai.azure.com
# 2. Créer un nouveau projet
# 3. Déployer un modèle (ex : gpt-4o-mini)
# 4. Copier le point de terminaison et la clé
```

#### 2. Configurer les Identifiants

```bash
# Option 1 : Azure CLI
az login

# Option 2 : Variables d'environnement
export AZURE_TENANT_ID="votre-tenant-id"
export AZURE_CLIENT_ID="votre-client-id"
export AZURE_CLIENT_SECRET="votre-client-secret"
```

### Configuration Hugging Face

```bash
# Obtenir le token Hugging Face
# 1. Aller sur https://huggingface.co/settings/tokens
# 2. Créer un nouveau token avec permissions de lecture
# 3. Sauvegarder le token de manière sécurisée

# Configurer dans le code
headers = {
    "Authorization": "Bearer hf_votre_token_ici"
}
```

### Installation Complète Étape par Étape

#### Étape 1 : Cloner le Dépôt

```bash
git clone https://github.com/elbruno/251023-CodigoFest.git
cd 251023-CodigoFest
```

#### Étape 2 : Configurer le Serveur MCP World Cup

```bash
cd MCP/worldcup-info

# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -e .[dev]
```

#### Étape 3 : Configurer le Serveur MCP Weather

```bash
cd ../SampleWeather

# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -e .[dev]
```

#### Étape 4 : Configurer l'Agent

```bash
cd ../../Agents

# Installer les dépendances de l'agent
pip install agent-framework
pip install agent-framework-azure-ai
pip install azure-identity

# Éditer worldcupinfo-v1.py
# - Mettre à jour ENDPOINT avec votre endpoint Azure
# - Mettre à jour MODEL_DEPLOYMENT_NAME avec votre modèle
# - Mettre à jour l'en-tête Authorization avec votre token HF
```

#### Étape 5 : Configurer les Projets C#

```bash
cd ../src

# Restaurer tous les projets
dotnet restore

# Compiler la solution
dotnet build
```

---

## 💡 Exemples d'Utilisation

### Scénario 1 : Interroger des Informations sur la Coupe du Monde

```python
# Dans Agent Builder ou MCP Inspector

# Question 1
"Quelles sont les villes hôtes de la Coupe du Monde 2026 au Mexique ?"

# Réponse attendue :
# - Mexico City (Estadio Azteca)
# - Guadalajara (Estadio Akron)
# - Monterrey (Estadio BBVA)

# Question 2
"Quand est la finale et où sera-t-elle jouée ?"

# Réponse attendue :
# 19 juillet 2026 au MetLife Stadium, New Jersey, USA
```

### Scénario 2 : Générer des Images Thématiques

```python
# L'utilisateur demande une image
"Générez une image en style pixel art de la mascotte de la Coupe du Monde jouant au football"

# L'agent :
# 1. Construit un prompt descriptif avec style pixelisé
# 2. Appelle gr1_flux1_schnell_infer
# 3. Retourne l'image et les métadonnées
```

### Scénario 3 : Conversation Multi-tours

```python
# Tour 1
Utilisateur : "Combien d'équipes participeront à la Coupe du Monde 2026 ?"
Agent : "48 équipes participeront à la Coupe du Monde 2026..."

# Tour 2
Utilisateur : "Et combien de matchs seront joués au total ?"
Agent : "Un total de 104 matchs sera joué..."

# Tour 3
Utilisateur : "Générez une image d'un stade rempli de supporters"
Agent : [Génère une image en style pixel art]
```

### Scénario 4 : Débogage avec MCP Inspector

```bash
# 1. Démarrer Inspector
cd MCP/worldcup-info/inspector
npm install
npm run dev

# 2. Ouvrir le navigateur sur http://localhost:5173

# 3. Se connecter au serveur MCP

# 4. Tester les outils :
# - List Tools
# - Sélectionner get_host_cities
# - Input : {"country": "Canada"}
# - Run Tool

# 5. Voir la réponse JSON avec les villes canadiennes
```

---

## 🔧 Dépannage

### Problème : Erreur lors de l'installation des dépendances Python

```bash
# Solution 1 : Mettre à jour pip
python -m pip install --upgrade pip

# Solution 2 : Utiliser uv (plus rapide)
pip install uv
uv venv
uv pip install -r pyproject.toml --extra dev
```

### Problème : Erreur d'authentification Azure

```bash
# Solution 1 : Se reconnecter avec Azure CLI
az login
az account show

# Solution 2 : Vérifier les variables d'environnement
echo $AZURE_TENANT_ID
echo $AZURE_CLIENT_ID

# Solution 3 : Utiliser DefaultAzureCredential interactif
# Dans le code, assurez-vous d'utiliser :
# DefaultAzureCredential(exclude_environment_credential=False)
```

### Problème : MCP Inspector ne se connecte pas

```bash
# Vérifier que le serveur MCP est en cours d'exécution
# Dans VS Code, panneau Debug → "Debug SSE in Inspector"

# Vérifier le port (par défaut 3001)
curl http://localhost:3001

# Si le port est occupé, changer dans :
# - .vscode/tasks.json
# - .vscode/launch.json
# - src/__init__.py
# - .aitk/mcp.json
```

### Problème : Erreur de génération d'images

```bash
# Vérifier le token Hugging Face
# Le token doit avoir des permissions de lecture

# Vérifier que le modèle est disponible
# https://huggingface.co/evalstate/flux1_schnell

# Vérifier les paramètres de génération
# width et height : 256-2048
# num_inference_steps : 1-16
# seed : 0-2147483647
```

### Problème : Le projet C# ne compile pas

```bash
# Nettoyer et reconstruire
dotnet clean
dotnet restore
dotnet build

# Vérifier la version de .NET
dotnet --version

# Si le SDK est manquant, installer depuis :
# https://dotnet.microsoft.com/download
```

### Problème : VS Code ne trouve pas l'interpréteur Python

```bash
# 1. Recharger VS Code après avoir créé venv
# 2. Commande : "Python: Select Interpreter"
# 3. Sélectionner : .venv/bin/python

# S'il n'apparaît pas :
which python  # Linux/Mac
where python  # Windows

# Ajouter le chemin manuellement dans les paramètres VS Code
```

---

## 📊 Architecture du Système

### Diagramme des Composants

```
┌─────────────────────────────────────────────────────────┐
│                  Utilisateur / Client                    │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Microsoft Agent Framework                   │
│  ┌────────────────────────────────────────────────┐    │
│  │  ChatAgent avec instructions personnalisées    │    │
│  │  - Traitement du langage naturel               │    │
│  │  - Gestion du contexte multi-tours             │    │
│  │  - Routage des intentions                      │    │
│  └────────────┬───────────────────────────────────┘    │
└───────────────┼──────────────────────────────────────────┘
                │
        ┌───────┴───────┐
        ▼               ▼
┌──────────────┐  ┌──────────────────┐
│ Azure AI     │  │ Outils MCP       │
│ Foundry      │  │                  │
│              │  │  ┌────────────┐  │
│ - GPT-4o     │  │  │ brunoHF    │  │
│ - GPT-4o     │  │  │ (Hugging   │  │
│   mini       │  │  │  Face)     │  │
│              │  │  └────────────┘  │
└──────────────┘  └─────────┬────────┘
                            │
                    ┌───────┴────────┐
                    ▼                ▼
        ┌──────────────────┐  ┌──────────────┐
        │ Serveur MCP      │  │ Modèle       │
        │ worldcup-info    │  │ FLUX1        │
        │                  │  │ Schnell      │
        │ - tournament_info│  │              │
        │ - host_cities    │  │ Génération   │
        │ - match_schedule │  │ d'images     │
        └──────────────────┘  └──────────────┘
```

### Flux de Données

1. **Entrée Utilisateur** : Question ou demande en langage naturel
2. **Traitement de l'Agent** : Analyse de l'intention et du contexte
3. **Routage** : Décision sur les outils à utiliser
4. **Exécution des Outils** : Appels aux serveurs MCP ou APIs
5. **Agrégation** : Combiner les réponses de plusieurs sources
6. **Génération de Réponse** : Format JSON structuré
7. **Retour à l'Utilisateur** : Réponse avec raisonnement et résultats

---

## 🎓 Concepts Clés

### Model Context Protocol (MCP)

**Qu'est-ce que c'est ?**
Un protocole ouvert qui standardise comment les applications fournissent du contexte aux LLMs.

**Avantages :**
- ✅ Réutilisabilité des outils entre différentes applications
- ✅ Séparation claire entre logique métier et IA
- ✅ Débogage et tests faciles
- ✅ Sécurité et contrôle d'accès

**Composants :**
- **Serveur** : Expose des outils et ressources
- **Client** : Consomme des outils (ex : Agent Framework)
- **Transport** : Communication (stdio, HTTP, SSE)

### Microsoft Agent Framework

**Qu'est-ce que c'est ?**
Framework pour construire des agents capables de raisonner, planifier et exécuter des tâches complexes.

**Fonctionnalités :**
- 🧠 Intégration avec Azure AI et modèles OpenAI
- 🔧 Support pour les outils et l'appel de fonctions
- 💬 Gestion des conversations multi-tours
- 🔄 Streaming des réponses
- 🔌 Connectivité avec serveurs MCP

**Cas d'Usage :**
- Assistants virtuels intelligents
- Automatisation des processus d'entreprise
- Analyse de documents
- Génération de contenu
- Recherche et synthèse d'informations

### Azure AI Foundry

**Qu'est-ce que c'est ?**
Plateforme unifiée pour développer, entraîner, évaluer et déployer des solutions d'IA.

**Services Clés :**
- 🤖 Azure OpenAI Service
- 🎯 Model Catalog
- 🧪 Prompt Flow
- 📊 Evaluation Tools
- 🚀 Deployment Options

---

## 🚀 Prochaines Étapes

### Pour les Développeurs

1. **Explorer les exemples** : Exécutez chaque démo pour comprendre le flux
2. **Modifier les prompts** : Expérimentez avec différentes instructions pour les agents
3. **Créer votre propre serveur MCP** : Utilisez les modèles comme base
4. **Intégrer avec vos données** : Connectez l'agent à vos propres sources d'information
5. **Déployer en production** : Déployez sur Azure Container Instances ou App Service

### Pour en Savoir Plus

#### Tutoriels Recommandés
- [Documentation MCP](https://modelcontextprotocol.io/docs)
- [Microsoft Agent Framework Quickstart](https://github.com/microsoft/agent-framework)
- [Azure AI Foundry Learning Path](https://learn.microsoft.com/azure/ai-services)

#### Ressources Supplémentaires
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers)
- [AI Toolkit Documentation](https://github.com/microsoft/vscode-ai-toolkit)
- [Hugging Face Documentation](https://huggingface.co/docs)

### Pour Expérimenter

#### Idées de Projets

1. **Assistant de Voyage pour la Coupe du Monde**
   - Intégrer des APIs de vols et d'hôtels
   - Recommandations de matchs personnalisées
   - Génération d'itinéraires

2. **Bot d'Analyse d'Équipes**
   - Interroger les statistiques historiques
   - Prédire les résultats
   - Générer des visualisations

3. **Générateur de Contenu pour Réseaux Sociaux**
   - Créer des publications automatiques sur les matchs
   - Générer des images promotionnelles
   - Calendrier de publication

4. **Chatbot d'Entreprise**
   - Se connecter à la base de données d'entreprise
   - Répondre aux questions des employés
   - Automatiser les tâches répétitives

---

## 📞 Contact et Support

### Auteur
**Bruno Capuano (elbruno)**
- GitHub : [@elbruno](https://github.com/elbruno)
- Événement : [CodigoFest](https://codigofacilito.com/codigofest)

### Communauté
- Participez aux discussions GitHub
- Signalez les problèmes et bugs
- Contribuez avec des pull requests
- Partagez vos projets basés sur ces démos

### Ressources d'Aide
- [GitHub Issues](https://github.com/elbruno/251023-CodigoFest/issues)
- [Azure Support](https://azure.microsoft.com/support)
- [MCP Community](https://github.com/modelcontextprotocol/discussions)

---

## 📝 Notes Finales

### Recommandations

1. **Sécurité** : Ne partagez jamais les tokens ou identifiants dans le code
2. **Coûts** : Surveillez l'utilisation d'Azure AI pour éviter les frais inattendus
3. **Limites de Taux** : Respectez les limites des APIs (Hugging Face, Azure)
4. **Tests** : Testez minutieusement avant la production
5. **Journalisation** : Implémentez la journalisation pour le débogage et l'audit

### Limitations Connues

- Les serveurs MCP actuels sont pour démonstration
- Les données de la Coupe du Monde 2026 peuvent changer
- La génération d'images dépend de la disponibilité de Hugging Face
- Les projets C# sont des modèles de base

### Contributions Bienvenues

Ce projet est ouvert aux contributions :
- 🐛 Signaler des bugs
- ✨ Proposer de nouvelles fonctionnalités
- 📝 Améliorer la documentation
- 🌍 Traduire dans d'autres langues
- 💡 Partager des cas d'usage

---

**Merci d'utiliser ces démos de CodigoFest 2023 !**

🎉 Nous espérons que ce contenu vous aidera à explorer les dernières nouveautés en IA de l'écosystème Azure.

---

**Licence** : MIT License  
**Dernière Mise à Jour** : Octobre 2023  
**Version** : 1.0.0
