def add_student(self, input_details):
    try:
        # All Logic here
        print(input_details)
        res = self.mongo_obj.insert_record(input_details)

        if res:

            return {"message": "Student added successfully", "status": "success"}
        else:
            return {'message': "", "status": "failed"}
    except Exception as e:
        # Log the exception
        return {'message': "", "status": "failed", "error": str(e)}