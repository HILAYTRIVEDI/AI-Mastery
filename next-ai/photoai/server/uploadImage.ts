'use server'

import {UploadApiResponse , v2 as cloudinary} from 'cloudinary';
import { actionClient } from '@/lib/safeAction';
import z from 'zod';



cloudinary.config({
    cloud_name: process.env.NEXT_PUBLIC_CLOUDNARY_CLOUD_NAME,
    api_key: process.env.NEXT_PUBLIC_CLOUDNARY_KEY,
    api_secret: process.env.NEXT_PUBLIC_CLOUDNARY_SECRET
})

const formData = z.object({
    image: z.instanceof(FormData)
})

export const uploadImage = actionClient
.schema(formData)
.action( async ({ parsedInput : {image} }) => {
    const formImage = image.get('image');

    if(!formImage) return {error: 'No image found in form data'};
    if( !image ) return {error: 'No image found in form data'};

    const file = formImage as File;

    try{
        const arryBuffer = await file.arrayBuffer();
        const buffer = Buffer.from(arryBuffer);
        

        return new Promise<UploadApiResponse>((resolve, reject) => {
            const uploadStream = cloudinary.uploader.upload_stream({
                upload_preset: process.env.CLOUDNARY_CLOUD_NAME
            }, (error, result) => {
                if(error || !result) {
                    reject(error);
                } else {
                    resolve(result);
                }
            }   
        );
        uploadStream.end(buffer);
        });
    } catch(error) {
        return {error: error}
    }

} )