from fastapi import APIRouter
from services.script_generation import generate_script
from services.avatar_generation import generate_avatar

router = APIRouter()

@router.post("/script")
async def generate_presentation_script(ppt_path: str, voice_sample_path: str):
    script = generate_script(ppt_path, voice_sample_path)
    return {"message": "Script generated successfully", "script": script}

@router.post("/avatar")
async def generate_presentation_avatar(face_image_path: str, voice_sample_path: str, avatar_type: str):
    avatar_path = generate_avatar(face_image_path, voice_sample_path, avatar_type)
    return {"message": "Avatar generated successfully", "avatar_path": avatar_path}