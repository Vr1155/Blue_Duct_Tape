import { useEffect } from "react";

const useTitle = (title) => {
  useEffect(() => {
    document.title = `${title} - Blue duct Tape`;
  }, []);
};

export default useTitle;
