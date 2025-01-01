"use client";

import { uploadImage } from "@/server/uploadImage";
import { useDropzone } from "react-dropzone";
import { Card, CardContent } from "../ui/card";

export default function UploadImage()
{

    const {getRootProps, getInputProps, isDragActive} = useDropzone({
        maxFiles: 1,
        accept: {
            "image/*": [".jpg", ".jpeg", ".png", ".webp"],
        },
        onDrop: async (acceptedFiles, fileRejections) => {
            if(acceptedFiles.length > 0)
            {
                // Create a FormData instance
                const formData = new FormData();

                // Append the file to the FormData instance
                formData.append("image", acceptedFiles[0]);

                // Create a URL for the file
                const objectURL = URL.createObjectURL(acceptedFiles[0]);
                
                // State management to Create Layer, Set Active Layer, and Set Image URL
                const res = await uploadImage({image: formData});
                
            }
        }
    })

    return (
        <Card {...getRootProps()}>
            <CardContent>
                <input type="text"  {...getInputProps()} />
                <div>
                    <h1>Cool Animation</h1>
                    <p>{ isDragActive ? 'Drop Your Image' : 'Start By uploading Images'}</p>
                    <p>Supported formats jpeg, png, webp</p>
                </div>
            </CardContent>
        </Card>
    );
}