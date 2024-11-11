export const fetchClassifiedData = async () => {
    try{
        const response = await fetch('htps://localhost:5000/get-classified-events');
        const data= await response.json();
        return data;
    } catch (error){
        console.error("Error fetching classified data:");
    }
};