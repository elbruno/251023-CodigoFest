# CodigoFest 2023 - Entérate de lo más nuevo en IA en el ecosistema Azure

Este repositorio contiene las demos y contenido de la sesión **"Entérate de lo más nuevo en IA en el ecosistema Azure"** presentada en [CodigoFest](https://codigofacilito.com/codigofest).

📚 **Documentación disponible en:**
- 🇪🇸 [Español](./docs/README.es.md) (Principal)
- 🇬🇧 [English](./docs/README.en.md)
- 🇫🇷 [Français](./docs/README.fr.md)

## 🎯 Descripción General

Esta sesión explora las últimas novedades en Inteligencia Artificial dentro del ecosistema Azure, incluyendo:

### 📦 Componentes del Repositorio

1. **MCP Servers (Model Context Protocol)**
   - 🏆 **World Cup 2026 Info**: Servidor MCP con información sobre la Copa Mundial FIFA 2026
   - 🌤️ **Sample Weather**: Servidor MCP de ejemplo para consultas meteorológicas

2. **Agentes con Microsoft Agent Framework**
   - 🤖 Implementación de agentes en Python que integran servidores MCP
   - 💬 Conversación multi-turno con persistencia de contexto
   - 🎨 Generación de imágenes con Hugging Face

3. **Proyectos C# con Agent Framework**
   - 🔧 Tres proyectos de ejemplo en .NET

## 🚀 Inicio Rápido

### Requisitos Previos
- Python 3.8 o superior
- .NET SDK (para proyectos C#)
- Visual Studio Code con AI Toolkit
- Azure AI Foundry (para funcionalidad completa de agentes)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/elbruno/251023-CodigoFest.git
cd 251023-CodigoFest

# Configurar servidor MCP de World Cup 2026
cd MCP/worldcup-info
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -e .[dev]

# Configurar servidor MCP de Weather
cd ../SampleWeather
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## 📖 Documentación Detallada

Para información detallada sobre cada componente, consulte la documentación completa:

- **[Documentación en Español](./docs/README.es.md)** - Documentación principal con explicaciones detalladas
- **[Documentation in English](./docs/README.en.md)** - Complete English documentation
- **[Documentation en Français](./docs/README.fr.md)** - Documentation complète en français

## 🎓 Estructura del Proyecto

```
251023-CodigoFest/
├── MCP/                          # Servidores Model Context Protocol
│   ├── worldcup-info/           # Información Copa Mundial 2026
│   └── SampleWeather/           # Ejemplo de servidor meteorológico
├── Agents/                      # Agentes con Agent Framework
│   └── worldcupinfo-v1.py      # Agente de World Cup con generación de imágenes
├── src/                         # Proyectos C# con Agent Framework
│   ├── AgentFx-01/
│   ├── AgentFx-02/
│   └── AgentFx-03/
└── docs/                        # Documentación multilingüe
    ├── README.es.md
    ├── README.en.md
    └── README.fr.md
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.

## 📄 Licencia

Este proyecto está licenciado bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Bruno Capuano (elbruno)**
- GitHub: [@elbruno](https://github.com/elbruno)
- Evento: [CodigoFest](https://codigofacilito.com/codigofest)

## 🔗 Enlaces Útiles

- [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-services)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [AI Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)