# Stable Diffusion Fine-tuning avec DreamBooth

Ce projet implémente le fine-tuning du modèle **Stable Diffusion v1.5** à l’aide de **DreamBooth**, permettant de générer des images personnalisées à partir de descriptions textuelles.

## Étapes du projet

1. Préparation du dataset : collecte, nettoyage et normalisation des images.  
2. Configuration de l’environnement Python et installation des dépendances.  
3. Test du modèle Stable Diffusion v1.5 avant fine-tuning.  
4. Entraînement DreamBooth sur images personnalisées.  
5. Optimisation des hyperparamètres et évaluation des performances.  
6. Sauvegarde et déploiement du modèle fine-tuné sur HuggingFace.  
7. Génération d’images à partir de prompts textuels.  
8. Automatisation du pipeline et reproductibilité du workflow.

## Technologies utilisées

- PyTorch
- DreamBooth
- Stable Diffusion v1.5
- HuggingFace Diffusers
- Google Colab (GPU Tesla T4)

## Résultats

1. **Prompt :** Avatar with the inscription "outside", black and white picture of a photo of KDY person  
   ![1](generated_images/1.png)

2. **Prompt :** Digital portrait of a photo of KDY person, smooth brushwork, subtle lighting, professional expression  
   ![2](generated_images/2.png)

3. **Prompt :** Illustrated avatar of a photo of KDY person. Eyes are blue, bald on top. Wearing rimless glasses. 3D illustration  
   ![3](generated_images/3.png)

4. **Prompt :** Photo-style avatar painting of a photo of KDY person  
   ![4](generated_images/4.png)

5. **Prompt :** Create a chibi character art for a photo of KDY person, Asian man, black hair middle part, white sweater, shoulders-up headshot  
   ![5](generated_images/5.png)

6. **Prompt :** Avatar of KDY person, painted in a photorealistic style  
   ![6](generated_images/6.png)

7. **Prompt :** Illustrated avatar of KDY person, male passport-style portrait, small chin beard, long hair, mature facial features, light background  
   ![7](generated_images/7.png)

8. **Prompt :** Illustrated avatar of KDY person, based on the aesthetics of Hotline Miami characters  
   ![8](generated_images/8.png)

9. **Prompt :** KDY person as a stylized French avatar, wearing a beret and moustache, medium portrait, simple background, cartoonish but refined style  
   ![9](generated_images/9.png)

10. **Prompt :** Tactical male avatar of KDY person, bald head, small black beard with subtle white highlights, military-inspired look, serious and confident expression, modern tactical outfit, strong masculine features  
    ![10](generated_images/10.png)

## Références
- https://huggingface.co/docs/diffusers/training/dreambooth  
- https://www.dreambooth.fr/  
- https://en.wikipedia.org/wiki/DreamBooth  
- https://dreambooth.github.io/  
- https://huggingface.co/stabilityai/stable-diffusion-3.5-large

Yassine DARIF | 2025
