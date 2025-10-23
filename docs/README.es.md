# 🇪🇸 Documentación en Español - CodigoFest 2023

## Entérate de lo más nuevo en IA en el ecosistema Azure

Esta documentación proporciona una guía completa de las demos y contenidos presentados en CodigoFest 2023.

---

## 📑 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Servidores MCP](#servidores-mcp)
3. [Agentes con Microsoft Agent Framework](#agentes-con-microsoft-agent-framework)
4. [Proyectos C# Agent Framework](#proyectos-c-agent-framework)
5. [Guías de Instalación y Uso](#guías-de-instalación-y-uso)
6. [Ejemplos de Uso](#ejemplos-de-uso)
7. [Solución de Problemas](#solución-de-problemas)

---

## 🎯 Introducción

Este repositorio demuestra las capacidades más avanzadas de la Inteligencia Artificial en el ecosistema Azure, enfocándose en:

- **Model Context Protocol (MCP)**: Protocolo estándar para conectar herramientas y datos con sistemas de IA
- **Microsoft Agent Framework**: Framework para construir agentes inteligentes que pueden razonar y ejecutar tareas
- **Azure AI Foundry**: Plataforma completa para desarrollar, entrenar y desplegar soluciones de IA
- **Integración con Hugging Face**: Generación de imágenes con modelos avanzados

### ¿Qué es Model Context Protocol (MCP)?

MCP es un protocolo abierto que estandariza cómo las aplicaciones proporcionan contexto a los modelos de lenguaje grandes (LLMs). Permite que los agentes de IA accedan a:
- Datos empresariales
- Herramientas y APIs
- Servicios externos
- Sistemas de archivo local

---

## 🏆 Servidores MCP

### 1. World Cup 2026 Info Server

Servidor MCP especializado que proporciona información completa sobre la Copa Mundial FIFA 2026.

#### 📋 Características

- **Información del Torneo**: Fechas, sedes, número de equipos y partidos
- **Ciudades Anfitrionas**: Detalles de las 16 ciudades sede y sus estadios
- **Calendario de Partidos**: Estructura del torneo y fechas clave
- **Datos Históricos**: Hechos únicos sobre este mundial histórico

#### 🔧 Herramientas Disponibles

1. **get_tournament_info()**
   - Retorna información general del torneo
   - Sin parámetros requeridos
   - Respuesta en formato JSON

2. **get_host_cities(country: Optional[str])**
   - Obtiene información sobre ciudades sede
   - Parámetro opcional: filtrar por país ('United States', 'Canada', 'Mexico')
   - Incluye nombre del estadio, capacidad y tipo de partidos

3. **get_match_schedule()**
   - Retorna estructura del torneo y calendario
   - Información sobre fase de grupos y eliminatorias
   - Fechas clave y notas especiales

#### 📊 Datos del Mundial 2026

```json
{
  "nombre": "Copa Mundial FIFA 2026",
  "anfitriones": ["Estados Unidos", "Canadá", "México"],
  "fechas": "11 de junio - 19 de julio, 2026",
  "equipos": 48,
  "partidos": 104,
  "estadios": 16,
  "primer_mundial_tres_naciones": true
}
```

#### 🎯 Casos de Uso

```python
# Ejemplo 1: Información general del torneo
await get_tournament_info()

# Ejemplo 2: Ciudades de Estados Unidos
await get_host_cities(country="United States")

# Ejemplo 3: Calendario completo
await get_match_schedule()
```

#### 🚀 Cómo Ejecutar

```bash
cd MCP/worldcup-info

# Opción 1: Usar uv (recomendado)
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml --extra dev

# Opción 2: Usar pip
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Depurar con Agent Builder (VS Code)
# Presiona F5 y selecciona "Debug in Agent Builder"
```

#### 🧪 Probar con MCP Inspector

```bash
cd inspector
npm install

# Iniciar Inspector (desde VS Code Debug panel)
# Selecciona "Debug SSE in Inspector (Edge)" o "(Chrome)"
# F5 para iniciar

# En el navegador:
# 1. Click en "Connect"
# 2. Selecciona "List Tools"
# 3. Elige una herramienta y ejecútala
```

### 2. Sample Weather Server

Servidor MCP de ejemplo que proporciona datos meteorológicos simulados.

#### 📋 Características

- Servidor simple para demostración
- Datos meteorológicos aleatorios
- Base para crear servidores MCP personalizados

#### 🔧 Herramientas Disponibles

1. **get_weather(location: str)**
   - Retorna información meteorológica simulada
   - Parámetro requerido: ubicación (ciudad, estado, coordenadas)
   - Respuesta con temperatura y condición climática

#### 🎯 Ejemplo de Uso

```python
# Consultar clima de una ciudad
await get_weather(location="Toronto")

# Respuesta ejemplo:
# {
#   "location": "Toronto",
#   "temperature": "72°F",
#   "condition": "Sunny"
# }
```

#### 🚀 Cómo Ejecutar

```bash
cd MCP/SampleWeather

# Configurar entorno
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Depurar con Agent Builder
# F5 en VS Code con "Debug in Agent Builder"
```

---

## 🤖 Agentes con Microsoft Agent Framework

### WorldCup Info Agent v1

Agente inteligente que combina consultas sobre el Mundial 2026 con generación de imágenes en estilo pixel art.

#### 🎨 Capacidades Principales

1. **Consultas Informativas**
   - Responde preguntas sobre la Copa Mundial 2026
   - Accede a datos en tiempo real vía MCP
   - Proporciona información precisa y actualizada

2. **Generación de Imágenes**
   - Genera imágenes en estilo pixelado (pixel art, 8-bit)
   - Usa modelo FLUX1 Schnell vía Hugging Face
   - Parámetros personalizables (tamaño, seed, steps)

3. **Conversación Multi-turno**
   - Mantiene contexto entre preguntas
   - Thread persistente para conversaciones coherentes
   - Procesamiento de respuestas en streaming

#### ⚙️ Configuración Técnica

```python
# Endpoint de Azure AI Foundry
ENDPOINT = "https://bruno-realtime-resource.services.ai.azure.com/api/projects/bruno-realtime"
MODEL_DEPLOYMENT_NAME = "gpt-5-mini"

# Herramientas MCP
MCPStreamableHTTPTool(
    name="brunoHF",
    description="MCP server for brunoHF",
    url="https://huggingface.co/mcp?login"
)
```

#### 📝 Instrucciones del Agente

El agente está configurado para:

- **Idioma**: Español (por defecto), adaptable según solicitud del usuario
- **Generación de Imágenes**: Siempre en estilo pixelado usando FLUX1 Schnell
- **Formato de Respuesta**: JSON estructurado con razonamiento y conclusión
- **Seguridad**: Evita contenido con copyright, ofrece alternativas legales

#### 🔄 Flujo de Trabajo

```
Usuario → Pregunta
    ↓
Agente → Analiza intención
    ↓
¿Requiere imagen? → SÍ → Genera prompt descriptivo
    |                         ↓
    |                    Llama a gr1_flux1_schnell_infer
    |                         ↓
    NO                   Recibe URL de imagen
    ↓                         ↓
Consulta MCP Server ← ← ← ← ←
    ↓
Construye respuesta estructurada
    ↓
Usuario ← Respuesta JSON
```

#### 💬 Ejemplos de Conversación

**Ejemplo 1: Consulta Informativa**
```
Usuario: "¿Cuándo comienza el mundial de fútbol de 2026 y dónde se juega?"

Agente:
{
  "input": "¿Cuándo comienza el mundial de fútbol de 2026 y dónde se juega?",
  "razonamiento": [
    "Consulta sobre fechas y sedes del Mundial 2026",
    "Información obtenida del servidor MCP worldcup-info"
  ],
  "respuesta": "El Mundial FIFA 2026 comienza el 11 de junio de 2026 con el partido inaugural en el Estadio Azteca de Ciudad de México. El torneo se jugará en tres países: Estados Unidos (60 partidos), México (10 partidos) y Canadá (10 partidos). La final será el 19 de julio de 2026 en el MetLife Stadium de Nueva Jersey, Estados Unidos.",
  "image": null,
  "sources": ["MCP worldcup-info server"]
}
```

**Ejemplo 2: Generación de Imagen**
```
Usuario: "¿Puedes generar una imagen de un mapache jugando al fútbol en el mundial de 2026?"

Agente:
{
  "input": "Generar imagen de mapache jugando fútbol en Mundial 2026",
  "razonamiento": [
    "Usuario solicita imagen, debe generarse en estilo pixelado",
    "Usar herramienta gr1_flux1_schnell_infer de Hugging Face",
    "Evitar logos oficiales por copyright"
  ],
  "respuesta": "He generado una imagen pixelada en estilo 8-bit de un mapache jugando fútbol. La imagen tiene un estilo retro de videojuego clásico.",
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
    "notes": "Imagen sin logos oficiales para evitar problemas de copyright"
  }
}
```

#### 🚀 Cómo Ejecutar

```bash
# Instalar dependencias
pip install agent-framework
pip install agent-framework-azure-ai
pip install azure-identity

# Configurar variables de entorno (o editar el script)
export AZURE_AI_ENDPOINT="tu-endpoint"
export AZURE_AI_MODEL="tu-modelo"

# Ejecutar el agente
cd Agents
python worldcupinfo-v1.py
```

#### 🔑 Requisitos

- Azure AI Foundry Project
- Azure Default Credential configurado
- Token de Hugging Face (para generación de imágenes)
- Python 3.8+

#### 🎛️ Parámetros de Generación de Imágenes

```python
generation_parameters = {
    "prompt": "Descripción detallada (60-70 palabras)",
    "width": 1024,           # Rango: 256-2048
    "height": 1024,          # Rango: 256-2048
    "seed": 123456789,       # Opcional: 0-2147483647
    "randomize_seed": True,  # Si True, seed aleatorio
    "num_inference_steps": 4 # Rango: 1-16
}
```

---

## 🔧 Proyectos C# Agent Framework

### Estructura de los Proyectos

El directorio `src/` contiene tres proyectos de ejemplo en C# que demuestran el uso de Agent Framework:

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

### Estado Actual

Actualmente, estos proyectos contienen plantillas básicas de "Hello World". Son puntos de partida para:

1. **Integración con Azure AI Services**
2. **Implementación de agentes en .NET**
3. **Conexión con servidores MCP desde C#**
4. **Construcción de aplicaciones empresariales con agentes**

### 🚀 Compilar y Ejecutar

```bash
cd src/AgentFx-01

# Restaurar dependencias
dotnet restore

# Compilar
dotnet build

# Ejecutar
dotnet run
```

### 🔜 Desarrollo Futuro

Estos proyectos están preparados para implementar:

- ✅ Agentes conversacionales en C#
- ✅ Integración con Azure OpenAI
- ✅ Conexión con servidores MCP
- ✅ Procesamiento de documentos
- ✅ Automatización empresarial

---

## 📚 Guías de Instalación y Uso

### Requisitos del Sistema

#### Software Necesario
- **Python**: 3.8 o superior
- **Node.js**: 16.x o superior (para MCP Inspector)
- **.NET SDK**: 6.0 o superior (para proyectos C#)
- **Visual Studio Code**: Última versión
- **Git**: Para clonar el repositorio

#### Extensiones de VS Code Recomendadas
- AI Toolkit for VS Code
- Python Extension
- C# Extension
- Python Debugger

### Configuración de Azure

#### 1. Azure AI Foundry Project

```bash
# Crear un proyecto en Azure AI Foundry
# 1. Ir a https://ai.azure.com
# 2. Crear nuevo proyecto
# 3. Desplegar modelo (ej: gpt-4o-mini)
# 4. Copiar endpoint y clave
```

#### 2. Configurar Credenciales

```bash
# Opción 1: Azure CLI
az login

# Opción 2: Variables de entorno
export AZURE_TENANT_ID="tu-tenant-id"
export AZURE_CLIENT_ID="tu-client-id"
export AZURE_CLIENT_SECRET="tu-client-secret"
```

### Configuración de Hugging Face

```bash
# Obtener token de Hugging Face
# 1. Ir a https://huggingface.co/settings/tokens
# 2. Crear nuevo token con permisos de lectura
# 3. Guardar token de forma segura

# Configurar en el código
headers = {
    "Authorization": "Bearer hf_tu_token_aqui"
}
```

### Instalación Completa Paso a Paso

#### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/elbruno/251023-CodigoFest.git
cd 251023-CodigoFest
```

#### Paso 2: Configurar Servidor MCP World Cup

```bash
cd MCP/worldcup-info

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -e .[dev]
```

#### Paso 3: Configurar Servidor MCP Weather

```bash
cd ../SampleWeather

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -e .[dev]
```

#### Paso 4: Configurar Agente

```bash
cd ../../Agents

# Instalar dependencias del agente
pip install agent-framework
pip install agent-framework-azure-ai
pip install azure-identity

# Editar worldcupinfo-v1.py
# - Actualizar ENDPOINT con tu endpoint de Azure
# - Actualizar MODEL_DEPLOYMENT_NAME con tu modelo
# - Actualizar Authorization header con tu token de HF
```

#### Paso 5: Configurar Proyectos C#

```bash
cd ../src

# Restaurar todos los proyectos
dotnet restore

# Compilar solución
dotnet build
```

---

## 💡 Ejemplos de Uso

### Escenario 1: Consultar Información del Mundial

```python
# En Agent Builder o MCP Inspector

# Pregunta 1
"¿Cuáles son las ciudades sede del Mundial 2026 en México?"

# Respuesta esperada:
# - Ciudad de México (Estadio Azteca)
# - Guadalajara (Estadio Akron)
# - Monterrey (Estadio BBVA)

# Pregunta 2
"¿Cuándo es la final y dónde se jugará?"

# Respuesta esperada:
# 19 de julio de 2026 en MetLife Stadium, Nueva Jersey, USA
```

### Escenario 2: Generar Imágenes Temáticas

```python
# Usuario solicita imagen
"Genera una imagen en estilo pixel art de la mascota del mundial jugando fútbol"

# El agente:
# 1. Construye prompt descriptivo con estilo pixelado
# 2. Llama a gr1_flux1_schnell_infer
# 3. Retorna imagen y metadatos
```

### Escenario 3: Conversación Multi-turno

```python
# Turno 1
Usuario: "¿Cuántos equipos participarán en el Mundial 2026?"
Agente: "48 equipos participarán en el Mundial 2026..."

# Turno 2
Usuario: "¿Y cuántos partidos se jugarán en total?"
Agente: "Se jugarán 104 partidos en total..."

# Turno 3
Usuario: "Genera una imagen de un estadio lleno de aficionados"
Agente: [Genera imagen en estilo pixel art]
```

### Escenario 4: Debugging con MCP Inspector

```bash
# 1. Iniciar Inspector
cd MCP/worldcup-info/inspector
npm install
npm run dev

# 2. Abrir navegador en http://localhost:5173

# 3. Conectar al servidor MCP

# 4. Probar herramientas:
# - List Tools
# - Seleccionar get_host_cities
# - Input: {"country": "Canada"}
# - Run Tool

# 5. Ver respuesta JSON con ciudades canadienses
```

---

## 🔧 Solución de Problemas

### Problema: Error al instalar dependencias de Python

```bash
# Solución 1: Actualizar pip
python -m pip install --upgrade pip

# Solución 2: Usar uv (más rápido)
pip install uv
uv venv
uv pip install -r pyproject.toml --extra dev
```

### Problema: Error de autenticación de Azure

```bash
# Solución 1: Re-login con Azure CLI
az login
az account show

# Solución 2: Verificar variables de entorno
echo $AZURE_TENANT_ID
echo $AZURE_CLIENT_ID

# Solución 3: Usar DefaultAzureCredential interactivo
# En el código, asegúrate de usar:
# DefaultAzureCredential(exclude_environment_credential=False)
```

### Problema: MCP Inspector no conecta

```bash
# Verificar que el servidor MCP esté corriendo
# En VS Code, Debug panel → "Debug SSE in Inspector"

# Verificar puerto (por defecto 3001)
curl http://localhost:3001

# Si el puerto está ocupado, cambiar en:
# - .vscode/tasks.json
# - .vscode/launch.json
# - src/__init__.py
# - .aitk/mcp.json
```

### Problema: Error de generación de imágenes

```bash
# Verificar token de Hugging Face
# El token debe tener permisos de lectura

# Verificar que el modelo esté disponible
# https://huggingface.co/evalstate/flux1_schnell

# Verificar parámetros de generación
# width y height: 256-2048
# num_inference_steps: 1-16
# seed: 0-2147483647
```

### Problema: Proyecto C# no compila

```bash
# Limpiar y reconstruir
dotnet clean
dotnet restore
dotnet build

# Verificar versión de .NET
dotnet --version

# Si falta SDK, instalar desde:
# https://dotnet.microsoft.com/download
```

### Problema: VS Code no encuentra el intérprete de Python

```bash
# 1. Recargar VS Code después de crear venv
# 2. Comando: "Python: Select Interpreter"
# 3. Seleccionar: .venv/bin/python

# Si no aparece:
which python  # Linux/Mac
where python  # Windows

# Agregar ruta manualmente en VS Code settings
```

---

## 📊 Arquitectura del Sistema

### Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────┐
│                     Usuario / Cliente                    │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Microsoft Agent Framework                   │
│  ┌────────────────────────────────────────────────┐    │
│  │  ChatAgent con instrucciones personalizadas    │    │
│  │  - Procesamiento de lenguaje natural          │    │
│  │  - Gestión de contexto multi-turno            │    │
│  │  - Routing de intenciones                     │    │
│  └────────────┬───────────────────────────────────┘    │
└───────────────┼──────────────────────────────────────────┘
                │
        ┌───────┴───────┐
        ▼               ▼
┌──────────────┐  ┌──────────────────┐
│ Azure AI     │  │ Herramientas MCP │
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
        │ MCP worldcup-    │  │ FLUX1        │
        │ info Server      │  │ Schnell      │
        │                  │  │ Model        │
        │ - tournament_info│  │              │
        │ - host_cities    │  │ Generación   │
        │ - match_schedule │  │ de imágenes  │
        └──────────────────┘  └──────────────┘
```

### Flujo de Datos

1. **Entrada del Usuario**: Pregunta o solicitud en lenguaje natural
2. **Procesamiento del Agente**: Análisis de intención y contexto
3. **Routing**: Decisión de qué herramientas usar
4. **Ejecución de Herramientas**: Llamadas a MCP servers o APIs
5. **Agregación**: Combinar respuestas de múltiples fuentes
6. **Generación de Respuesta**: Formato estructurado JSON
7. **Retorno al Usuario**: Respuesta con razonamiento y resultados

---

## 🎓 Conceptos Clave

### Model Context Protocol (MCP)

**¿Qué es?**
Un protocolo abierto que estandariza cómo las aplicaciones proporcionan contexto a LLMs.

**Ventajas:**
- ✅ Reutilización de herramientas entre diferentes aplicaciones
- ✅ Separación clara entre lógica de negocio y IA
- ✅ Fácil debugging y testing
- ✅ Seguridad y control de acceso

**Componentes:**
- **Server**: Expone herramientas y recursos
- **Client**: Consume herramientas (ej: Agent Framework)
- **Transport**: Comunicación (stdio, HTTP, SSE)

### Microsoft Agent Framework

**¿Qué es?**
Framework para construir agentes que pueden razonar, planificar y ejecutar tareas complejas.

**Características:**
- 🧠 Integración con Azure AI y modelos de OpenAI
- 🔧 Soporte para herramientas y función calling
- 💬 Gestión de conversaciones multi-turno
- 🔄 Streaming de respuestas
- 🔌 Conectividad con MCP servers

**Casos de Uso:**
- Asistentes virtuales inteligentes
- Automatización de procesos empresariales
- Análisis de documentos
- Generación de contenido
- Búsqueda y síntesis de información

### Azure AI Foundry

**¿Qué es?**
Plataforma unificada para desarrollar, entrenar, evaluar y desplegar soluciones de IA.

**Servicios Clave:**
- 🤖 Azure OpenAI Service
- 🎯 Model Catalog
- 🧪 Prompt Flow
- 📊 Evaluation Tools
- 🚀 Deployment Options

---

## 🚀 Próximos Pasos

### Para Desarrolladores

1. **Explorar los ejemplos**: Ejecuta cada demo para entender el flujo
2. **Modificar prompts**: Experimenta con diferentes instrucciones para los agentes
3. **Crear tu propio MCP Server**: Usa las plantillas como base
4. **Integrar con tus datos**: Conecta el agente a tus propias fuentes de información
5. **Implementar en producción**: Despliega en Azure Container Instances o App Service

### Para Aprender Más

#### Tutoriales Recomendados
- [Documentación de MCP](https://modelcontextprotocol.io/docs)
- [Microsoft Agent Framework Quickstart](https://github.com/microsoft/agent-framework)
- [Azure AI Foundry Learning Path](https://learn.microsoft.com/azure/ai-services)

#### Recursos Adicionales
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers)
- [AI Toolkit Documentation](https://github.com/microsoft/vscode-ai-toolkit)
- [Hugging Face Documentation](https://huggingface.co/docs)

### Para Experimentar

#### Ideas de Proyectos

1. **Asistente de Viajes para el Mundial**
   - Integrar APIs de vuelos y hoteles
   - Recomendaciones personalizadas de partidos
   - Generación de itinerarios

2. **Bot de Análisis de Equipos**
   - Consultar estadísticas históricas
   - Predecir resultados
   - Generar visualizaciones

3. **Generador de Contenido para Redes Sociales**
   - Crear posts automáticos sobre partidos
   - Generar imágenes promocionales
   - Calendario de publicaciones

4. **Chatbot Empresarial**
   - Conectar a base de datos corporativa
   - Responder consultas de empleados
   - Automatizar tareas repetitivas

---

## 📞 Contacto y Soporte

### Autor
**Bruno Capuano (elbruno)**
- GitHub: [@elbruno](https://github.com/elbruno)
- Evento: [CodigoFest](https://codigofacilito.com/codigofest)

### Comunidad
- Participa en las discusiones de GitHub
- Reporta issues y bugs
- Contribuye con pull requests
- Comparte tus proyectos basados en estas demos

### Recursos de Ayuda
- [GitHub Issues](https://github.com/elbruno/251023-CodigoFest/issues)
- [Azure Support](https://azure.microsoft.com/support)
- [MCP Community](https://github.com/modelcontextprotocol/discussions)

---

## 📝 Notas Finales

### Recomendaciones

1. **Seguridad**: Nunca compartas tokens o credenciales en el código
2. **Costos**: Monitorea el uso de Azure AI para evitar cargos inesperados
3. **Rate Limits**: Respeta los límites de las APIs (Hugging Face, Azure)
4. **Testing**: Prueba exhaustivamente antes de producción
5. **Logging**: Implementa logging para debugging y auditoría

### Limitaciones Conocidas

- Los MCP servers actuales son para demostración
- Los datos del Mundial 2026 pueden cambiar
- La generación de imágenes depende de disponibilidad de Hugging Face
- Los proyectos C# son plantillas básicas

### Contribuciones Bienvenidas

Este proyecto está abierto a contribuciones:
- 🐛 Reportar bugs
- ✨ Proponer nuevas features
- 📝 Mejorar documentación
- 🌍 Traducir a otros idiomas
- 💡 Compartir casos de uso

---

**¡Gracias por usar estas demos de CodigoFest 2023!**

🎉 Esperamos que este contenido te ayude a explorar las últimas novedades en IA del ecosistema Azure.

---

**Licencia**: MIT License  
**Última actualización**: Octubre 2023  
**Versión**: 1.0.0
